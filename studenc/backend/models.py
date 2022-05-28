from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=999, unique=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=999)
    location = models.CharField(max_length=999)
    description = models.TextField(max_length=999)
    spots = models.IntegerField()
    code = models.IntegerField(unique=True)
    neto = models.FloatField(max_length=999)
    bruto = models.FloatField(max_length=999)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.code}"

    