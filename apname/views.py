from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_response(request):
    return HttpResponse("This is my first request")