🌍 AI Smart News Sphere

AI Smart News Sphere is a dual-mode intelligent news aggregator that combines advanced Natural Language Processing (NLP) with Generative AI to cluster, analyze, and provide deep insights into news stories.

This project features two distinct components:

Web Dashboard: A responsive, Thistle-themed web application powered by Google Gemini Pro for deep analysis (Sentiment, Root Cause, Historical Context).

Python CLI Engine: A robust backend script that fetches live news (NewsData.io & RSS), performs TF-IDF vectorization, and clusters topics using Scikit-Learn.

🚀 Features

🖥️ Web Dashboard (news_aggregator.html)

AI-Powered Analysis: Uses Google Gemini Pro to generate summaries, sentiment scores, and detailed insights.

Novelty Insights:

Root Cause Analysis: Explains the "why" behind the news.

Historical Context: Connects current events to past occurrences.

✨ Follow-up Questions: Generates insightful questions for further reading.

Modern UI: Responsive grid layout with a polished "Thistle" (Purple/White) aesthetic.

Smart Filtering: Filter news by Category, Location (USA/India), and Type.

🐍 Python CLI Engine (smart_newssphere.py)

Live Data Fetching: Pulls real-time articles from NewsData.io API and BBC RSS feeds.

Machine Learning Clustering: Uses TF-IDF Vectorization and Agglomerative Clustering to group related stories automatically.

Console Reporting: Displays structured text summaries and clustering stats in the terminal.

📂 Project Structure

NewsSphere/
│
├── news_aggregator.html    # MAIN WEB APP: The visual dashboard (Mock Data + Gemini AI)
│
├── smart_newssphere.py     # MAIN PYTHON SCRIPT: Entry point for the CLI aggregator
├── fetcher.py              # Module: Fetches data from APIs and RSS feeds
├── topic_clustering.py     # Module: Handles TF-IDF and Clustering logic
├── nlp_processor.py        # Module: Processes text for the Python CLI
│
└── README.md               # Project Documentation


🛠️ Prerequisites

To run this project, you need:

Python 3.8+ installed on your system.

API Keys:

Google Gemini API Key: For the Web Dashboard.

NewsData.io API Key: For the Python CLI live fetching.

📦 Installation

Clone or Download the project folder.

Install Python Dependencies (required for the Python CLI version):

Open your terminal/command prompt in the project folder and run:

pip install requests feedparser scikit-learn numpy


🖥️ How to Run: Web Dashboard

The web dashboard requires a local server to function correctly (to avoid browser security blocks).

Open your Command Prompt or PowerShell.

Navigate to your project directory:

cd path/to/NewsSphere


Start a Local Server:

python -m http.server 8000


Open your web browser (Edge, Chrome, etc.) and go to:
👉 http://localhost:8000/news_aggregator.html

🔑 Configuration:

To enable the AI features locally, open news_aggregator.html in a code editor.

Find the line const apiKey = ""; (around line 380).

Paste your Google Gemini API Key inside the quotes.

🐍 How to Run: Python CLI (Live Data)

This version runs in your terminal and fetches real-time news.

Open fetcher.py in a code editor.

Ensure your NewsData.io API Key is set in the NEWSDATA_API_KEY variable.

Run the main script:

python smart_newssphere.py


The script will fetch live articles, perform clustering algorithms, and print the grouped topics to your console.

🤖 Tech Stack

Frontend: HTML5, Tailwind CSS, Vanilla JavaScript.

Backend (CLI): Python, Scikit-Learn (Sklearn), NumPy.
