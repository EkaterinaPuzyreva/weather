from django.shortcuts import render
from django.http import HttpResponse
import redis
import requests




def index(request):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    token = '55a0ef4d81a24e47f86a2de2cd6854e5'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + token
    city = 'Krasnoyarsk'
    response = requests.get(url.format(city)).json()
    temp = response["main"]["temp"]
    r.set('city', city)
    r.set('temp', temp)
    r1 = r.get('city')
    r2 = r.get('temp')
    data = {"message": r1, "message1":r2 }
    return render(request, 'weather/index.html', context = data)

