import requests
latitude = 12.97
longitude = 77.59

url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m"
)
response = requests.get(url)
data=reponse.json()

temperature = data["current"]["temperature_2m"]
print(f"Current temperature:{temperature}°C")