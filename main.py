import requests
import json
import time
import keyboard

key = "" ##Put Your Key Here
url = "http://api.weatherapi.com/v1/current.json"


print('\n' * 100)
print("Heyas! Welcome to the Weather App!")
city = input('Please insert city name or zip code! (Make sure your spelling is correct!) :')

params = {
    "key": key,
    "q": city,
}



response = requests.get(url, params=params)
data = response.json()

data = response.json()


print('Heres all of the info about the weather in', data['location']['name'], data['location']['region'], '!')
print('')
print(data['current']['condition']['text'])
print('Temperature:', data['current']['temp_f'])
print('Feels Like:', data['current']['feelslike_f'])
print('')
print('')
print('')
print('Last Updated', data['current']['last_updated'], '. Powered by /www.weatherapi.com/')


## Heyas!