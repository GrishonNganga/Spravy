from flask import render_template, Blueprint
from frontend.requests import get_trending_articles, get_sources

news = Blueprint('news', __name__, template_folder='templates')

@news.route('/')
def index():
    sources_list = get_sources()

    return render_template('news/index.html', sources = sources_list)    

@news.route('/trending')
def trending():

    articles_list = get_trending_articles()
    return render_template('news/trending.html', articles = articles_list)