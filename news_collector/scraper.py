import os
import django
from newsapi import NewsApiClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_aggregator_project.settings")
django.setup()

from news_collector.models import NewsArticle

def get_top_headlines(api_key, country='us'):
    newsapi = NewsApiClient(api_key=api_key)

    try:
        # Get top headlines
        top_headlines = newsapi.get_top_headlines(country=country)

        if top_headlines['status'] == 'ok' and top_headlines['articles']:
            print(f"Found {len(top_headlines['articles'])} articles. Saving to database...")
            for article in top_headlines['articles']:
                # Create a new NewsArticle object and save it to the database
                NewsArticle.objects.create(
                    title=article['title'],
                    url=article['url'],
                    summary=article['description'],
                    sentiment='neutral' # We will add sentiment analysis later
                )
            print("Done! Articles saved to the database.")
        else:
            print("No headlines found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Your API key is already here
    api_key = 'babe50094d0c42069202f5c1ce82138e'
    get_top_headlines(api_key)