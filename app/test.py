from django.shortcuts import render
from django.http import HttpResponse 

def remote_list(request):
    return HttpResponse('remote is running')

def local_list(request):
    return HttpResponse('local is running')