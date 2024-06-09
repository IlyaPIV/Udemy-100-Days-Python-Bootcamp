import requests

api_key = "2701d9fe37f0efc26d4726002fef53b2"
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"


weather_params = {
    "lat": 52.40953,
    "lon": 16.931992,
    "exclude": "current, minutely, daily",
    "appid": api_key
}

response = requests.get(ENDPOINT, params=weather_params)
print(response.json())
