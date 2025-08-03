from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello Saqib, This is your First Project!</h1>")
def item(request):
    return HttpResponse("Hello Saqib, This is a item !")