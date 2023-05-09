import json, requests, sys


api_key = '81acc6acb02af547474ca2beac56f67f'
url = "https://api.openweathermap.org/data/2.5/weather"

location = input("Indicate Location in longitude and latitude separated by SPACE ")

latitude, longitude = location.split()

latitude = float(latitude)
longitude = float(longitude)

params = {
    "lat" : latitude,
    "appid": api_key,
    "lon": longitude
}
response = requests.get(url, params=params)
print(response.text)
response.raise_for_status()