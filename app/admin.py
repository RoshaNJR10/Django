from django.contrib import admin
from .models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=('name','address','roll','contact')
admin.site.register(student,studentAdmin)