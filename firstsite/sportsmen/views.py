from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def sports(request):
    return HttpResponse('<h1>Articles by sports</h1>')

def about(request):
    return HttpResponse('<h1>About us</h1>')

def contacts(request):
    return HttpResponse('<h1>Contact information</h1>')
