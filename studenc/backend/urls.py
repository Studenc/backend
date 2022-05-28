
from django.urls import path

from . import views



urlpatterns = [
    path('getcompanies/', views.getCompanyList, name='getcompanies'),
    path('getjobs/', views.getJobs, name='getjobs'),
    path('postcompany/', views.postCompany, name='postcompany'),
    path('postjob/', views.postJob, name='postjob'),
]