from django.contrib import admin
from testapp.models import Employee

class EmployeeModel(admin.ModelAdmin):
    list_display = ['id','name','addr','sal']
    list_filter = ['name','sal']
    search_fields = ('name',)
    ordering = ['id']

admin.site.register(Employee,EmployeeModel)