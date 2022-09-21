from __future__ import unicode_literals

from django.contrib import admin
from app_name.models import Employee

# Register your models here.


class EmployeeAdmin (admin.ModelAdmin):
    list_display = ['username','firstName','lastName','email','birthDate','basicSalary','status','group','description']
    search_fields = ['username', 'firstName', 'email', 'birthDate']
    list_per_page = 25

admin.site.register(Employee, EmployeeAdmin)