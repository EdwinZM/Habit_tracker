import requests 
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
token = "ekobonita"
username = "edwinzm23"
habit = input("What is the habit you'd like to track? ")
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

response = requests.post(url=pixela_endpoint, json=user_params)

print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "float",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": token
}

requests.post(url=graph_endpoint, json=graph_params, headers=headers)

today = datetime.datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input(f"how long did you {habit} today? ")
}

response = requests.post(url=f"{graph_endpoint}/graph1", json=pixel_params, headers=headers)
print(response.text)