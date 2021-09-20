import requests


YouCity = input("Введите город: ")
api_key = "40df1398d96b7259c68a34c53615c4ac"

def request(city, key):
	res = requests.get(f"http://api.openweathermap.org/data/2.5/find", params = {'q': city, 'type': 'link', 'APPID': key})

	data = res.json()
	temp = data['list'][0]['main']['temp']
	Tc = temp - 273.15

	return int(Tc)


print("Температура: " + str(request(YouCity, api_key)) + "°")