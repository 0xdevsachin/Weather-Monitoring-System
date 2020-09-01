import requests 

location = input("Enter The Location : ")
api = input("Enter The Location : ")
URL=f"https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
r = requests.post(url = URL) 
data = r.json()


temp = data['main']['temp']
humid = data['main']['humidity']
visible  = data['visibility']
speed = data['wind']['speed']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
pressure = data['main']['pressure']
name  = data['name']



