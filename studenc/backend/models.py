from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    
class Servis(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    spots = models.IntegerField()
    code = models.IntegerField()
    neto = models.FloatField()
    bruto = models.FloatField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    servis = models.ForeignKey(Servis, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    