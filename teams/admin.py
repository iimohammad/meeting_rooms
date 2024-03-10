# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
# from .models import *
#
#
# @admin.register(CustomUser)
# class UserAdmin(DefaultUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {
#             'fields': (
#                 'first_name',
#                 'last_name',
#                 'email',
#                 'phone_number',
#                 'team',
#                 'image',
#             )
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active',
#                 'is_staff',
#                 'is_superuser',
#                 'groups',
#                 'user_permissions'
#             ),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#
#     list_display = (
#         'username',
#         'email',
#         'first_name',
#         'last_name',
#         'phone_number',
#         'team',
#         'is_staff',
#     )
#
#     search_fields = (
#         'username',
#         'first_name',
#         'last_name',
#         'phone_number',
#         'team',
#         'email',
#     )
#
#
# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ['name', 'company']
#     sortable_by = ['name', 'company']
#     list_filter = ['name']
#     search_fields = ['name', 'company']
#
#
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ['name', 'address']
#
#
# @admin.register(MeetingRoom)
# class MeetingRoomAdmin(admin.ModelAdmin):
#     list_display = ['name', 'company', 'capacity', 'available']
#
#
# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ['team', 'meeting_room', 'start_datetime', 'duration', 'status']
#     list_editable = ['status']
#
#
# @admin.register(Manager)
# class ManagerAdmin(admin.ModelAdmin):
#     list_display = ['user', 'team']
