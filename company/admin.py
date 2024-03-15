from django.contrib import admin
from .models import *


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'manager', 'permission', 'priority']
    sortable_by = ['name', 'company']
    list_filter = ['name']
    search_fields = ['name', 'company']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
