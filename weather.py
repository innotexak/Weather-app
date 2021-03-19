import requests 
from requests.exceptions import HTTPError
import json
def weather():
    
    greeting = "Welcome to Facade ventures weather app"
    print(greeting)
    name = str(input("Please enter your full name (Firstname Lastname): "))
    print(name + " welcome to Fecade Ventures")
    print("Please select one of the city number [1-5] below")
    a = 'Johannesburg'
    b = 'Lusaka'
    c = 'Abuja'
    d = 'Nairobi'
    e = 'Accra'
    print(1, a)
    print(2, b)
    print(3, c)
    print(4, d)
    print(5, e)
    city = int(input("Please select the city number here: "))
    if city == 1:
        api_city = a
        country = "South Africa"
        print("You selected ", a)
    elif city == 2:
        api_city = b
        country = "Zambia"
        print("You selected ", b)
    elif city == 3:
        api_city = c
        country = "Nigeria"
        print("You selected ", c)
    elif city == 4:
        api_city = d
        country = "Kenya"
        print("You selected ", d)
    elif city == 5:
        api_city = e
        country = "Ghana"
        print("You selected ", e)
    
    api_key ='a670aae98eb56d4e2aca533972074e76' 
    url = f'https://api.openweathermap.org/data/2.5/weather?q={api_city}&appid={api_key}'
    # url ="https://community-open-weather-map.p.rapidapi.com/weather"
    try:
        response = requests.get(url)
    except HTTPError as err:
        print(f'Http Error occurred: {err}')
        
    else:
        
        print(f" {name} Please wait while we retrieve your information \n Retrieving infor for {api_city} State in {country}...")
        json_response = response.json()
        # print(json_response)
        description = json_response['weather'][0]['description']
        cloud = json_response['clouds']['all']
        wind = json_response['wind']['speed']
        min_temp = json_response['main']['temp_min']
        mc_temp =(min_temp - 273.15)
        max_temp = json_response['main']['temp_max']
        xc_temp =(max_temp - 273.15)
    
        print(f'Todays forecast for {api_city} State is {description} \n It is also {cloud}% cloudy in {api_city} state today \n with minimum temperature of {int(mc_temp)}°C and \n maximum temperature of {int(xc_temp)}°C \n the wind blows at {wind}m/s ' )
weather()
