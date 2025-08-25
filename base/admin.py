from django.contrib import admin

# Register your models here.
from .models import studentform
class cadminmodel(admin.ModelAdmin):
    list_display=['id','ename','rollno','course','mobileno','image']
    list_display_links=['ename']
    ordering=['id']
admin.site.register(studentform,cadminmodel)
