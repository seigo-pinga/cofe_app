from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import datetime
from .models import Coffee

def index(request):
    city = 'tokyo'
    api_key = '3ff67ba107d57f802c04a2640e7d8557'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ja'
#http://api.openweathermap.org/data/2.5/weather?q=tokyo&appid=3ff67ba107d57f802c04a2640e7d8557
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': round(data['main']['temp'], 1),
                'humidity': data['main']['humidity'],
                'weather': data['weather'][0]['description'],
                'atmospheric_pressure': data['main']['pressure'],
            }
    except requests.RequestException:
        pass
    if request.method == 'POST':
        pass
    print(weather_data)

    if request.method == 'POST':
        # フォームから送信されたデータを取得
        data = datetime.datetime.now()
        bean_amount = request.POST.get('bean_amount')
        bean_grind = request.POST.get('bean_grind')
        bean_rost = request.POST.get('bean_rost')
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        weather = request.POST.get('weather')
        atmospheric_pressure = request.POST.get('atmospheric_pressure')

        Coffee.objects.create(
                date=data,
                bean_amount=bean_amount,
                bean_grind=bean_grind,
                bean_rost=bean_rost,
                temperature=temperature,
                humidity=humidity,
                weather=weather,
                atmospheric_pressure=atmospheric_pressure,
                )
        return redirect('index')

    context = {
        'weather_data': weather_data,
        }
    
    return render(request, 'index.html', context)

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def another_view(request):
    latest_log = Coffee.objects.latest('data')
    print(latest_log)
