from django.contrib import admin
from .models import application,District,Branch
# Register your models here.
admin.site.register(application)
admin.site.register(District)
admin.site.register(Branch)