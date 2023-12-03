from django.shortcuts import render
from .forms import Product
from django.http import HttpResponse


def clients(request):
    return render(request, "clients.html", {})


def info(request):
    return render(request, "info.html")


def add(request):
    return render(request, "add.html")


def addProduct(request):
    form = Product()
    return render(request, "product.html", {'form': form})
