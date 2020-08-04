from app.home import home
from flask import render_template, redirect, url_for


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/animation')
def animation():
    return render_template('home/animation.html')


@home.route('/search')
def search():
    return render_template('home/search.html')
