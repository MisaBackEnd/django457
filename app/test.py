from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
import requests

def index(request):
    return HttpResponse('is running')
