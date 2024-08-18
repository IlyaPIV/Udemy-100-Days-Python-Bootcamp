import smtplib
from mail_creds import APP_EMAIL, APP_PASS


def send_email(addr, msg):
    my_email = APP_EMAIL
    app_password = APP_PASS
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=addr,
            msg=f"Subject:Amazon Right Price\n\n{msg}")
