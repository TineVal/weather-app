import requests
from django.shortcuts import render
from .models import RecentSearch

def index(request):
    weather_data = {}
    error = None
    recent_searches = RecentSearch.objects.order_by('-timestamp')[:5]  # Gets the last 5 searches

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()  
        if not city:
            error = "City name cannot be empty!"
        else:
            api_key = 'f8a8276afb73de42300153d9c2ae2d3d'
            forecast_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

            try:
                response = requests.get(forecast_url, timeout=10)
                response.raise_for_status()
                data = response.json()

                if data.get('cod') != 200:
                    error = data.get('message', 'Error fetching weather data.')
                else:
                    weather_data = {
                        'city': data['name'],
                        'temperature': data['main']['temp'],
                        'description': data['weather'][0]['description'],
                        'icon': data['weather'][0]['icon'],
                    }

                    # Save to recent searches
                    RecentSearch.objects.create(city=data['name'])

            except requests.exceptions.RequestException as e:
                error = f"Network error: {e}"

    return render(request, 'weather/index.html', {
        'weather_data': weather_data,
        'error': error,
        'recent_searches': recent_searches,
    })
