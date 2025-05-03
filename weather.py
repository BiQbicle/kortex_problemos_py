import requests

api_key = "df08a8c8b9730f470ea7f31118f60df8"

city_input = input("Enter a city to get weather data: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=imperial&APPID={api_key}")
farenheittocelsisu = (weather_data.json()['main']['temp'] - 32) * 5/9
print(farenheittocelsisu)
print(weather_data.json()['weather'][0]['description'])