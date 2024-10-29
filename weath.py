import requests
import syek

city = input('''Напишите название города:
''')

res = requests.get('https://api.openweathermap.org/data/2.5/weather', params= {'q' : city, 'units' : 'metric', 'lang' : 'RU', 'APPID' : syek.key})
data = res.json()

print('Город:', city)
print('Погодные условия:', data['weather'][0]['description'])
print('Температура:', data['main']['temp'])
print('Мин. температура:', data['main']['temp_min'])
print('Макс. температура:', data['main']['temp_max'])

print(data)