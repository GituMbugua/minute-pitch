from flask import render_template, redirect, url_for
from . import main
from ..models import Category, Review

@main.route('/')
def index():
    '''
    view root page function that returns index page
    '''
    category = Category.get_categories()

    title = 'Home'
    return render_template('index.html', title = title, category = category)

@main.route('/category/<int:id>')
def category(id):
    '''
    view category function that returns the pitches of that category
    '''
    category = Category.query.get(id)

    return render_template('category.html', category = category)