from django.conf import settings
from django.shortcuts import render
from . forms import CityForm
import requests

# Create your views here.
def weather_summary(request):
    if request.method=='POST':
        api_key = settings.API_KEY
        
        formdata = CityForm(request.POST)
        if formdata.is_valid(): # This is a technique used by Django to check the input field is clean from any malicious code
            city_entered_by_user = formdata.cleaned_data['city']

            response = requests.get("http://api.weatherapi.com/v1/current.json?key="+api_key+"&q="+city_entered_by_user+"").json() # This line is used to get the data from the API in JSON format. json() parses the HTTP response to a Python dictionary and allows us to access JSON data using Python objects like response['current']['temp_c']...
            citydata = {
                "temp":response['current']['temp_c'],
                "condition":response['current']['condition']['text'], # ['text'] is used to get the text value from the dictionary
                "icon":response['current']['condition']['icon'],
            }
            
            return render(request, 'weatherapp/summary.html', {"form": formdata, "city": city_entered_by_user, "citydata": citydata})
        
    return render(request, 'weatherapp/summary.html', {"form": CityForm})

def weather_loop(request):
    return render(request, 'weatherapp/loop.html', {})