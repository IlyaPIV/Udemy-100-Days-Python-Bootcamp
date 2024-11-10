import os.path

from dominate.svg import title
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import DecimalField
from wtforms.validators import DataRequired, NumberRange
import requests

MOVIE_DB_SEARCH_URL = 'some_API_URL'
MOVIE_DB_API_KEY = 'some_API_KEY'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my-top-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


class RateMovieForm(FlaskForm):
    rating = DecimalField(label='Your rating Out of 10 e.g. 7.6', places=1,
                          validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class FindMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    if not os.path.isfile('my-top-movies.db'):
        db.create_all()
    all_movies = db.session.query(Movie).order_by(Movie.rating.asc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies = all_movies)


@app.route('/add', methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route('/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    edit_form = RateMovieForm()
    movie = Movie.query.get_or_404(movie_id)
    if edit_form.validate_on_submit():
        movie.review = edit_form.review.data
        movie.rating = edit_form.rating.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie = movie, form = edit_form)


@app.route('/delete/<int:movie_id>')
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
