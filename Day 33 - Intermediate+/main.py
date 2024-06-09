import time

import requests
import smtplib
from datetime import datetime

MY_LATITUDE = 52.406376
MY_LONGITUDE = 16.925167
MY_EMAIL = "moloch.by@gmail.com"
APP_PASSWORD = "ywdxgxwzkyqknpru"


def is_iss_overhead():
    response = requests.get(url="https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    iss_position = (iss_longitude, iss_latitude)
    print(f"ISS positions is : {iss_position}")

    #Your position is within +/-5 degrees of the current ISS position
    if (MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5) and (MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    time_now = datetime.now()
    print(f"Current time is: {time_now}")

    sunrise_hr = int(sunrise.split("T")[1].split(":")[0])
    sunset_hr = int(sunset.split("T")[1].split(":")[0])
    if time_now.hour >= sunset_hr or time_now.hour <= sunrise_hr:
        return True


while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look up\n\nThe ISS is above you in the sky")
    time.sleep(60)
