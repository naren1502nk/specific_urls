from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse('<h1> hello function is running</h1>')
