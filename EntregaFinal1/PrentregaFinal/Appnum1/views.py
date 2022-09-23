from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "Appnum1/inicio.html")

def trabajadores(request):
    return render(request, "Appnum1/colab.html")

def compradores(request):
    return render(request, "Appnum1/buyer.html")

def vendedores(request):
    return render(request, "Appnum1/seller.html")

