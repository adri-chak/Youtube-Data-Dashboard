import streamlit as st
import pandas as pd
from googleapiclient.discovery import build

API_KEY = st.secrets["YOUTUBE_API_KEY"]
youtube = build('youtube', 'v3', developerKey=API_KEY)

st.set_page_config(page_title="YouTube Pro Dashboard", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True) 

def get_channel_info(c_id):
    request = youtube.channels().list(part="snippet,statistics", id=c_id)
    response = request.execute()
    return response['items'][0]

def get_video_analytics(c_id):
    search_res = youtube.search().list(part="snippet", channelId=c_id, maxResults=10, order="date", type="video").execute()
    
    v_ids = [item['id']['videoId'] for item in search_res['items']]
    v_titles = [item['snippet']['title'] for item in search_res['items']]
    v_dates = [item['snippet']['publishedAt'] for item in search_res['items']]

    stats_res = youtube.videos().list(part="statistics", id=','.join(v_ids)).execute()
    
    views = [int(item['statistics'].get('viewCount', 0)) for item in stats_res['items']]
    likes = [int(item['statistics'].get('likeCount', 0)) for item in stats_res['items']]

    df = pd.DataFrame({
        'Date': pd.to_datetime(v_dates).date,
        'Title': v_titles,
        'Views': views,
        'Likes': likes
    })
    df['Engagement %'] = round((df['Likes'] / df['Views']) * 100, 2)
    return df

st.sidebar.title("🚀 Analysis Center")
channel_id = st.sidebar.text_input("YouTube Channel ID", "UCX6OQ3DkcsbYNE6H8uQQuVA")
run_btn = st.sidebar.button("Fetch Live Analytics")

if run_btn:
    ch_data = get_channel_info(channel_id)
    df = get_video_analytics(channel_id)

    col_img, col_text = st.columns([1, 5])
    with col_img:
        st.image(ch_data['snippet']['thumbnails']['default']['url'], width=100)
    with col_text:
        st.title(ch_data['snippet']['title'])
        st.write(ch_data['snippet']['description'][:200] + "...")

    st.divider()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Subscribers", f"{int(ch_data['statistics']['subscriberCount']):,}")
    m2.metric("Avg Views/Video", f"{int(df['Views'].mean()):,}")
    m3.metric("Highest Engagement", f"{df['Engagement %'].max()}%")
    m4.metric("Total Videos Scanned", len(df))

    st.subheader("📊 Performance Trends")
    st.line_chart(df, x='Date', y='Views')

    st.subheader("📋 Video Breakdown")
    st.dataframe(df, use_container_width=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Excel/CSV Report", data=csv, file_name="yt_report.csv")