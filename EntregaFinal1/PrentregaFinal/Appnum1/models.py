from django.db import models

# Create your models here.

class colaboradores(models.Model):

    colab_nombre = models.CharField(max_length=40)
    colab_apellido = models.CharField(max_length=40)
    colab_edad = models.IntegerField()
    colab_fecha_ingreso = models.DateField()
    colab_categoria_venta = models.CharField(max_length=60)

class compradores(models.Model):

    buyer_nombre = models.CharField(max_length=40)
    buyer_apellido = models.CharField(max_length=40)
    buyer_email = models.EmailField()
    buyer_direccion = models.CharField(max_length=70)
    buyer_tlf = models.IntegerField()

class sellers(models.Model):

    seller_nombre = models.CharField(max_length=40)
    seller_categoria = models.CharField(max_length=50)
    seller_email = models.EmailField()