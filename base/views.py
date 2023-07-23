from bs4 import BeautifulSoup
from django.shortcuts import render
import requests
from requests.compat import quote_plus
from . import models


BASE_CRAIGSLIST_URL = 'https://kerala.craigslist.org/search/bbb?query={}'



# Create your views here.
def home(request):
    return render(request , 'base/index.html')

def search(request):
    # getting the search value
    search_values = request.POST.get('search')
    #passing the search value into Search data model
    models.Search.objects.create(search=search_values)
    #quote_plus used to fill the white space with +eses
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search_values))
    #The . get() method sends a request for data to a web server. The response object it returns contains various types of data such as the webpage text, status code, and the reason for that response.
    respose = requests.get(final_url)
    data = respose.text
    soup = BeautifulSoup(data,'html.parser')
    #telling to soup in the html code and find all the list and in list class called cl-static-search-result 
    post_listing = soup.find_all('li',{'class' : 'cl-static-search-result'})
    print(post_listing)
    # print(post_listing)
    final_posting = []
    for post in post_listing:
        post_title = post.find(class_='title').text
        post_url = post.find('a').get('href')
        post_location = post.find(class_='location').text
        final_posting.append((post_title,post_url,post_location))
    print(final_posting)    

    #passing this to search.html to the front-end using dictionary
    front_end_stuff = {
        'search' : search_values,
        'final_posting' : final_posting,
    }   
    return render(request, 'base/search.html',front_end_stuff)