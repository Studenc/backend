from django.contrib import admin

from .models import APIAccessKey, Company, Job

# Register your models here.
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(APIAccessKey)
