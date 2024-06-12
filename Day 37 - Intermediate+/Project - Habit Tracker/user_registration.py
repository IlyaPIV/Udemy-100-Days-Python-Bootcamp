import requests

PIXELA_ENDPOINT = "https://www.pixe.la/v1/users"

USER_NAME = "moloch-san"

user_params = {
    "token": "qwerty12345",
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)
