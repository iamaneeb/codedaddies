from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request , 'base/index.html')

def search(request):
    search_values = request.POST.get('search')
    front_end_stuff = {
        'search' : search_values
    }
    return render(request, 'base/search.html',front_end_stuff)