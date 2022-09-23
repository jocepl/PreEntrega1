from django.urls import path
from Appnum1.views import *

urlpatterns = [
    path("", inicio),
    path("trabajadores/", trabajadores),
    path("compradores/", compradores),
    path("vendedores/", vendedores),
]