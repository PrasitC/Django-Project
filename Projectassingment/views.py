from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render
from country.models import Country 
from city.models import City # replace 'country_app' with your app's name

def homep(request):
    #return render(request=)
   
   #return HttpResponse("Hello World!")
  return render(request, "../templates/header.html")
def city(request):
    return redirect('city:city-list')

def city_detail(request, slug):
    city = get_object_or_404(City, slug=slug)
    return render(request, 'city_detail.html', {'city': city})



def country(request):
     return redirect('country:country-list')




def country_detail(request, slug):
    country = get_object_or_404(Country, slug=slug)
    return render(request, 'country_detail.html', {'country': country})