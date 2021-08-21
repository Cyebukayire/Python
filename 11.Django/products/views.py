from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello! Welcome to our store")


def products(request):
    return HttpResponse("PRODUCTS!")


def new(request):
    return HttpResponse("NEW PRODUCTS!")


