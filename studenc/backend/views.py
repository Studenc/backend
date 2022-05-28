from urllib.error import HTTPError
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views import View
from rest_framework import generics
from django.db.utils import IntegrityError
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

    
    
def getCompanyList(request):
    companies = models.Company.objects.values("id", "name")
    data = json.dumps(list(companies))
    
    return HttpResponse(data, content_type="application/json")

def getJobs(request):
    jobs = models.Job.objects.values("id", "title", "location", "description", "spots", "code", "neto", "bruto", "phone", "email", "contact", "company", "date")
    data = json.dumps(list(jobs), default=str)
    
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def postCompany(request):
    try:
        company = models.Company(name=request.POST["name"])
        company.save()
        company = models.Company.objects.values("id", "name").get(name=request.POST["name"])
        data = json.dumps(company)
        return HttpResponse(data, content_type="application/json")
    except IntegrityError:
        company = models.Company.objects.values("id", "name").get(name=request.POST["name"])
        data = json.dumps(company)
        return HttpResponse(data, content_type="application/json")
    
@csrf_exempt
def postJob(request):
    try:
        company = models.Company.objects.get(name=request.POST["company"])
        job = models.Job(title=request.POST["title"], 
                         location=request.POST["location"], 
                         description=request.POST["description"], 
                         spots=request.POST["spots"], 
                         code=request.POST["code"], 
                         neto=request.POST["neto"], 
                         bruto=request.POST["bruto"], 
                         phone=request.POST["phone"], 
                         email=request.POST["email"], 
                         contact=request.POST["contact"], 
                         company=company)
        job.save()
    except IntegrityError:
        return HTTPError(400, "Job ID already exists")