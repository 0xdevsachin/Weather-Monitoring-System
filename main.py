import requests 
import platform
import time

location = input("\nEnter The Location : ")
have_api = input("\nDo You have API Key y/n : ")
if have_api == 'y' or have_api == 'Y':
	api = input("\nEnter The API KEY : ")
	timing = input("\nDo you want regular data or only once (r/o) :")
	if timing == 'r' :
		try:
			interval = int(input("\nAt what time interval you need notification : "))  #Specify the minutes after which you need the notification
			how_much_time = int(input("\nFor how much time you need notification : ")) #Specify the hour you need the notification
		except :
			print("\nEnter Valid Value (☉｡☉)!")
	else:
		interval = 0
elif have_api == 'n' or have_api == 'N':
	print("\nGo To https://openweathermap.org and get your API Key ʘ‿ʘ")
	exit()

else:
	print("\nEnter Correct Choice (☉｡☉)!")
	exit()

def weather_report():
	URL=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api}"
	r = requests.post(url = URL) 
	data = r.json()
	return(data)



def linux():
	import gi
	gi.require_version('Notify', '0.7')
	from gi.repository import Notify,GdkPixbuf
	
	Notify.init("Weather Report")
	notification = Notify.Notification.new(
    str("Weather Report"),
    str(f"Name: {name}\nHumidity: {humid}\nSpeed: {speed}\nTemperature: {temp}"))

	image = GdkPixbuf.Pixbuf.new_from_file("weather.png")
	notification.set_image_from_pixbuf(image)

	notification.show()
# 	To close the notification and with will also save your meomory
# 	notification.close()



def window_notify():
	from win10toast import ToastNotifier
	toaster = ToastNotifier()

	toaster.show_toast("Weather Report", f"""Name: {name}\nHumidity: {humid}\nSpeed: {speed}\nTemperature: {temp}""", threaded=True,icon_path="weather.ico", duration=3) 

	toaster.notification_active()

def main():

	
	data = weather_report()
	global temp,humid,visible,speed,sunrise,sunset,pressure,name
	temp  = data['main']['temp']
	humid = data['main']['humidity']
	visible  = data['visibility']
	speed = data['wind']['speed']
	sunrise = data['sys']['sunrise']
	sunset = data['sys']['sunset']
	pressure = data['main']['pressure']
	name  = data['name']

	os  = platform.system()
	if os == "Windows" :
		window_notify()
	if os == "Linux":
		linux()

if interval == 0:
	main()
else:
	current = time.time()
	while(1):
		after = time.time()
		if (after - current) > (how_much_time*3600):
			break
		main()
		time.sleep(interval*60)










