from django.contrib import admin

from .models import APIAccessKey, Company, Job, StatRecord

# Register your models here.
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(APIAccessKey)
admin.site.register(StatRecord)
