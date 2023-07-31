from django.shortcuts import render
from requests import get

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=8fc1d7abf9ad6278cb17608da1c347e5&units=metric"
        
        response = get(url).json()

        description = response['weather'][0]['description']
        icon = response['weather'][0]['icon']
        temperature = response['main']['temp']
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']

        imageURL = "https://openweathermap.org/img/wn/"+ icon +"@2x.png"
        print(f'Icon: {imageURL}')

        context = {
            'city': city,
            'description':description,
            'temperature':temperature,
            'humidity':humidity,
            'wind_speed':wind_speed,
            'imageURL': imageURL
        }

    return render(request, 'result.html', context) 