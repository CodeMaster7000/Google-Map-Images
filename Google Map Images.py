import requests

# Enter your api key here
api_key = "_your_api_key_"
url = "https://maps.googleapis.com/maps/api/staticmap?"
center = "London"

zoom = 12
r = requests.get(url + "center =" + center + "&zoom =" +
				str(zoom) + "&size = 500x500&key =" +
							api_key + "sensor = false")

f = open('address of the file location ', 'wb')
f.write(r.content)
f.close()
