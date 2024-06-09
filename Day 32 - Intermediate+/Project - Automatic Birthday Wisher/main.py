import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = "moloch.by@gmail.com"
APP_PASSWORD = "ywdxgxwzkyqknpru"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    template_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(template_path) as letter_file:
        contents = letter_file.read()
        contents =  contents.replace("[NAME]", person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}")
