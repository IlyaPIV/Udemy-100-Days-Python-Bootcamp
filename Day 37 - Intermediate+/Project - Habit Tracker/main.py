import requests
from datetime import datetime

TOKEN = "qwerty12345"
USER_NAME = "moloch-san"
GRAPH_ID = "graph1"
API_ENDPOINT = "https://www.pixe.la/v1/users"
PIXEL_ENDPOINT = f"{API_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"
# https://pixe.la/v1/users/moloch-san/graphs/graph1.html

headers = {
    "X-USER-TOKEN": TOKEN
}

# INSERT DATA
# todays_date = datetime(year=2024, month=3, day=13)
todays_date = datetime.now()
quantity_amount = int(input("How many lessons did you complete today? "))
pixel_data = {
    "date": todays_date.strftime("%Y%m%d"),
    "quantity": str(quantity_amount)
}
response = requests.post(url=PIXEL_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)


# UPDATE DATA
updated_date = todays_date.strftime("%Y%m%d")
UPDATE_ENDPOINT = f"{API_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{updated_date}"

new_amount = quantity_amount + 5
updated_pixel_data = {
    "quantity": str(new_amount)
}
# response = requests.put(url=UPDATE_ENDPOINT, json=updated_pixel_data, headers=headers)
# print(response.text)

# DELETE DATA
deleted_date = updated_date
DELETE_ENDPOINT = f"{API_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{deleted_date}"
# response = requests.delete(DELETE_ENDPOINT, headers=headers)
# print(response.text)
