import urllib, json
from .models import Article


def configure_request(app):
    global news_api_key, news_base_url
    news_api_key = app.config['NEWS_API_KEY']
    news_base_url = app.config['NEWS_API_BASE_URL']        

def get_trending_articles():
    trending_articles_endpoint = news_base_url.format('top-headlines','language=en', news_api_key)
    with urllib.request.urlopen(trending_articles_endpoint)as url:
        trending_articles = url.read()
        trending_articles = json.loads(trending_articles)

        trending_articles = trending_articles['articles']
        trending_articles_list = process_articles(trending_articles)

    return trending_articles_list

    
def process_articles(articles_list):
    articles_list_object = []
    for article in articles_list:
        article_title = article['title']
        if len(article_title) > 65:
            article_title = article_title[:65] + '...'
        an_article = Article(article['url'], article_title, article['description'], article['urlToImage'], article['source']['name'], article['publishedAt'])
        articles_list_object.append(an_article)

    return articles_list_object

    
