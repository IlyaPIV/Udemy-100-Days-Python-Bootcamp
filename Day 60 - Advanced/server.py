from flask import Flask, render_template, request
import smtplib

OWN_EMAIL = 'YOUR OWN EMAIL ADDRESS'
OWN_PASSWORD = 'YOUR EMAIL ADDRESS PASSWORD'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("test.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # do something
    if request.method == "POST":
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


def send_email(name, email, phone, message):
    email_msg = f'Subject:New message from FLASK\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_msg)


if __name__ == '__main__':
    app.run(debug=True)