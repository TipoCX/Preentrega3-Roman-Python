from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(xx):
    return HttpResponse("<h1>Este es el index de forms</h1>")
