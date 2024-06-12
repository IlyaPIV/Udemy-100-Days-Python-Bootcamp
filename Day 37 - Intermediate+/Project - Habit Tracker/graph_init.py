import requests

TOKEN = "qwerty12345"
USER_NAME = "moloch-san"
PIXELA_ENDPOINT = "https://www.pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "duolingo",
    "unit": "lesson",
    "type": "int",
    "color": "shibafu"
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)
# https://pixe.la/v1/users/moloch-san/graphs/graph1.html
