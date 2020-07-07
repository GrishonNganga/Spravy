import urllib, json
from .models import Article, Source


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

def get_sources():
    sources_endpoint = news_base_url.format('sources', '', news_api_key)
    with urllib.request.urlopen(sources_endpoint)as url:
        sources = url.read()
        sources = json.loads(sources)

        sources = sources['sources']
        sources_list = process_sources(sources)

    return sources_list
    
def process_sources(sources_list):
    sources_list_object = []
    for source in sources_list:
        a_source = Source(source['id'] ,source['name'], source['description'], source['url'], source['category'])
        sources_list_object.append(a_source)

    return sources_list_object

def get_source_articles(source):
    source_endpoint = news_base_url.format('everything', 'sources={}'.format(source), news_api_key )

    with urllib.request.urlopen(source_endpoint)as url:
        source_articles = url.read()
        source_articles = json.loads(source_articles)
        source_articles = source_articles['articles']
        source_articles_object = process_articles(source_articles)

    return source_articles_object


def process_articles(articles_list):
    articles_list_object = []
    for article in articles_list:
        article_title = article['title']
        if len(article_title) > 65:
            article_title = article_title[:65] + '...'
        an_article = Article(article['source']['id'], article['url'], article_title, article['description'], article['urlToImage'], article['source']['name'], article['publishedAt'])
        articles_list_object.append(an_article)

    return articles_list_object
