from flask import Flask, render_template
import requests

posts = requests.get('https://api.npoint.io/8547cb8abeb3751541bc').json()
app = Flask(__name__)


@app.route('/')
def index():
    header_title = 'Home'
    return render_template("contact.html", header_title=header_title, all_posts=posts)

@app.route('/about')
def about():
    header_title = 'About'
    return  render_template("about.html", header_title=header_title)

@app.route('/contact')
def contact():
    header_title = 'Contact'
    return render_template('contact.html', header_title=header_title)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == post_id:
            requested_post = blog_post
            break
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
