from django.http import HttpResponse
import json
from django.db.utils import IntegrityError
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
    
    
def getCompanyList(request):
    companies = models.Company.objects.values("id", "name")
    data = json.dumps(list(companies))
    
    return HttpResponse(data, content_type="application/json")

def getJobs(request):
    jobs = models.Job.objects.values("id", "title", "location", "description", "spots", "code", "neto", "bruto", "phone", "email", "contact", "company", "date")
    data = json.dumps(list(jobs), default=str)
    
    return HttpResponse(data, content_type="application/json")

def searchJobs(request):
    query = request.GET.get("query")
    svector = SearchVector("title", "description", "code", "location", "company__name")
    squery = SearchQuery(query)
    results = models.Job.objects.annotate(search=svector, rank=SearchRank(svector, squery)).filter(search=squery).order_by("-rank").values("id", "title", "location", "description", "spots", "code", "neto", "bruto", "phone", "email", "contact", "company", "date")
    data = json.dumps(list(results), default=str)
    
    return(HttpResponse(data, content_type="application/json"))

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
        company = models.Company.objects.get(id=request.POST["company"])
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
        return HttpResponse("job posted successfully", status=200)
    except IntegrityError:
        return HttpResponse("job already exists", status=400)
    
def docs(request):
    template = loader.get_template('docs.html')
    return HttpResponse(template.render())