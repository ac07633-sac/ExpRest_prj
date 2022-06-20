from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'landing/index.html')

def home(request):
    return HttpResponse("<h1>Hello World HOME!</h1>")
