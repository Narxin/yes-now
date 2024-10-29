import requests
import telebot
import time
import syek 



bot = telebot.TeleBot(syek.token)

@bot.message_handler(commands=['start'])
def weather(message):
    bot.send_message(message.chat.id, 'Напишите название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip()
    
    res = requests.get('https://api.openweathermap.org/data/2.5/weather', params= {'q' : city, 'units' : 'metric', 'lang' : 'RU', 'APPID' : syek.key})
    data = res.json()

    bot.send_message(message.chat.id, f'Погодные условия : {data['weather'][0]['description']}')
    time.sleep(0.5)
    bot.send_message(message.chat.id, f'Мин. температура : {data['main']['temp_min']}')
    time.sleep(0.5)
    bot.send_message(message.chat.id, f'Температура : {data['main']['temp']}')
    time.sleep(0.5)
    bot.send_message(message.chat.id, f'Макс. температура : {data['main']['temp_max']}')
                
    
    

bot.infinity_polling()