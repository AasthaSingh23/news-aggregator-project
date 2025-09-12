from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    # A short headline for the article. It will be required.
    title = models.CharField(max_length=200)

    # The URL to the original news story.
    url = models.URLField(max_length=200)

    # The AI-generated summary of the article.
    summary = models.TextField()

    # The AI-generated sentiment (e.g., positive, negative, neutral).
    sentiment = models.CharField(max_length=50)

    # A list of keywords or topics extracted by the AI.
    topics = models.JSONField(default=list)

    # The date the article was published.
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title