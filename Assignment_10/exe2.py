import requests

api_key = "46a47d3338726c1ba9a7971320f8e6b1"
city = input("Enter municipality name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    
    print(f"Condition: {description}")
    print(f"Temperature: {temp_celsius:.1f} Celsius")
else:
    print("City not found")