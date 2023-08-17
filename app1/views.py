from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hai(request):
    return HttpResponse('<h1>your app1 hai fun is rinning<h1>')