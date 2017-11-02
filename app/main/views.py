from flask import render_template, redirect, url_for
from . import main
from .forms import PitchForm, ReviewForm
from ..models import Category, Pitch, Review
from flask_login import login_required, current_user

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
    title = f'{category.name} pitches'
    pitch = Pitch.get_pitches(category.id)

    return render_template('category.html', title = title, category = category, pitch = pitch)

@main.route('/category/pitch/new/<int:id>', methods = ["GET", "POST"])
@login_required
def new_pitch(id):
    '''
    view category that returns a form to create a pitch
    '''
    form = PitchForm()
    category = Category.query.filter_by(id = id).first()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data

        # pitch instance
        new_pitch = Pitch(category_id = category.id, title = title, post = post, user = current_user)

        # save pitch
        new_pitch.save_pitch()  
        return redirect(url_for('.category', id = category.id))
    title = f'{category.name} pitches'
    return render_template('new_pitch.html', title = title, pitch_form = form, category = category)

@main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    '''
    view category that returns a form to create a new review
    '''
    form = ReviewForm()
    pitch = Pitch.query.filter_by(id = id).first()
    if form.validate_on_submit():
        review = form.review.data

        # review instance
        new_review = Review(pitch_id = pitch.id, post_review = review, user = current_user)

        # save review 
        new_review.save_review()
        return redirect(url_for('.reviews', id = pitch.id ))

    title = f'{pitch.title} review'
    return render_template('new_review.html', title = title, review_form = form, pitch = pitch)

@main.route('/pitch/reviews/<int:id>')
def reviews(id):
    '''
    viw category that returns all reviews for a pitch
    '''
    pitch = Pitch.query.get(id)
    review = Review.get_reviews(pitch.id)
    title = f'{pitch.title} review'

    return render_template('reviews.html', title = title, pitch = pitch, review = review)