from flask import render_template, Blueprint, request
from frontend.requests import get_trending_articles, get_sources, get_source_articles

news = Blueprint('news', __name__, template_folder='templates')

@news.route('/')
def index():
    sources_list = get_sources()

    return render_template('news/index.html', sources = sources_list)    

@news.route('/trending')
def trending():

    articles_list = get_trending_articles()
    return render_template('news/trending.html', articles = articles_list)

@news.route('/source')
def show_source():
    url = request.args.get('domain', None)
    a_source_articles = get_source_articles(url)
    
    return render_template('news/source.html', articles = a_source_articles)

@news.route('/categories')
def show_categories():

    categories = ['general', 'technology', 'business', 'sports', 'entertainment', 'science']
    return render_template('news/categories.html',categories = categories )
