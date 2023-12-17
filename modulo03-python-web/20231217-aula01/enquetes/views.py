from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Olá mundo! Você está no site de enquetes.")
