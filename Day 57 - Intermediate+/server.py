from flask import Flask, render_template
import requests
import random
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 100)
    current_year = datetime.datetime.now().year
    return render_template("index.html", random_num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_data = requests.get(gender_url).json()
    # gender = random.choice(['Male', 'Female'])
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_data = requests.get(age_url).json()
    # age = random.randint(10, 80)
    age = age_data["age"]

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route('/blog')
def blog():
    url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url)
    full_data = response.json()
    return render_template("blog.html", posts=full_data)


if __name__ == '__main__':
    app.run(debug=True)
