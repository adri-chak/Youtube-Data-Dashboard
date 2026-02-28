# 🚀 YouTube Pro-Analyst Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Overview
This **Pro-Analyst Dashboard** transforms raw JSON data from the YouTube Data API v3 into actionable business intelligence. Built during my internship at **Soft Grow Tech**, this tool allows users to track engagement trends, visualize performance, and export data with a single click.

---

## 🔥 Features
* **Real-Time Analytics:** Fetches live data directly from Google's servers.
* **Engagement Scoring:** Custom-built algorithm to calculate `(Likes/Views) %` for true audience sentiment.
* **Visual Growth Trends:** Interactive line charts to visualize view counts across the latest videos.
* **Branding Sync:** Automatically pulls channel profile pictures and descriptions via the API.
* **Data Portability:** One-click CSV export for offline deep-dive analysis.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Backend:** [Google API Client Library](https://github.com/googleapis/google-api-python-client)
* **Data Handling:** [Pandas](https://pandas.pydata.org/)
* **Security:** Managed via `.streamlit/secrets.toml` and `.gitignore`.

---
