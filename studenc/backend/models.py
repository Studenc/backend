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
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} - {self.code}"
    
class APIAccessKey(models.Model):
    key = models.CharField(max_length=999)
    name = models.CharField(max_length=999)
    
    def __str__(self):
        return self.name
    
class StatRecord(models.Model):
    date = models.DateField(auto_now_add=True, unique=True) # limit myself to one a day poggers, will most likely be inserted by the weekly scraper cron job TODO
    numofjobs = models.IntegerField() # number of all job records
    numofcompanies = models.IntegerField() # number of all companies
    numofactivejobs = models.IntegerField() # number of all active jobs
    average_neto = models.FloatField() # average neto of active jobs
    average_bruto = models.FloatField() # average bruto of active jobs
    delta_neto = models.FloatField() # delta average_neto
    delta_bruto = models.FloatField() # delta average_bruto
    
    def __str__(self):
        return f"{self.date}"

    