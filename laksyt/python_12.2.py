
import requests

api_key = "cc924f1207a587f41b5ae5af419d1b73"
kaupunki = input("Anna paikkakunta: ")

url = "https://api.openweathermap.org/data/2.5/weather"
print("API-avaimen pituus:", len(api_key))
params = {
    "q": kaupunki,
    "appid": api_key,
    "lang": "fi",
    "units": "metric"
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Säätila:", data["weather"][0]["description"])
    print("Lämpötila:", data["main"]["temp"], "°C")
else:
    print("Virhe:", response.json().get("message"))
