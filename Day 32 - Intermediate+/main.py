import smtplib
import datetime as dt
import random


def send_email(addr, msg):
    my_email = "moloch.by@gmail.com"
    app_password = "ywdxgxwzkyqknpru"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=addr,
            msg=f"Subject:Monday Motivation\n\n{msg}")


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
        send_email("petermoloch@mail.ru", quote)
