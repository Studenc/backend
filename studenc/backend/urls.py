
from django.urls import path

from . import views



urlpatterns = [
    path('getcompanies/', views.getCompanyList, name='getcompanies'),
    path('getjobs/', views.getJobs, name='getjobs'),
    path('postcompany/', views.postCompany, name='postcompany'),
    path('postjob/', views.postJob, name='postjob'),
    path('docs/', views.docs, name='docs'),
    path('search/jobs/', views.searchJobs, name='searchjobs'),
    path('search/companies/', views.searchCompanies, name='searchcompanies'),
]