import requests
import bs4
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("hello treasure nepal")
    names = []
    d = {
        'names': names,
        'collage': 'ncit'
    }

    page = requests.get("https://fabpedigree.com/james/mathmen.htm")
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    name = soup.findAll("li")
    # li = []
    for n in name:
        s = n.find('a')
        names.append(s.string)

    return render(request, "home.htm", d)


def bootcamp(request):
    return HttpResponse("inside bootcamp")
