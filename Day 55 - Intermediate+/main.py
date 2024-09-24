from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def bold_result():
        return '<b>' + function() + '</b>'
    return bold_result


def make_emphasis(function):
    def emphasis_result():
        return '<em>' + function() + '</em>'
    return emphasis_result


def make_underlined(function):
    def underline_result():
        return '<u>' + function() + '</u>'
    return underline_result


@app.route('/')
def hello_world():
    return '<h1 style=text-align: center>Hello World!</h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


@app.route("/username/<name>")
def greet(name):
    return f'Hello, {name}!'


@app.route("/username/<name>/<int:number>")
def long_greeting(name, number):
    return f'Hello, {name}! You are {number} years old!'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return '<b>Bye!</b>'


if __name__ == '__main__':
    app.run(debug=True)
