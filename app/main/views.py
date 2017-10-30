from flask import render_template, redirect, url_for
from . import main
from ..models import Review

@main.route('/')
def index():
    '''
    view root page function that returns index page
    '''
