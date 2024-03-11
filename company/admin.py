# from django.contrib import admin
# from .models import *
#
#
# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ['name', 'company']
#     sortable_by = ['name', 'company']
#     list_filter = ['name']
#     search_fields = ['name', 'company']
#     list_editable = ['name']
#
#
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ['name', 'address']
#
#
#
from django.contrib import admin
from .models import Company , Team

admin.site.register(Company)
admin.site.register(Team)