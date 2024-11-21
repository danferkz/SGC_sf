# employees/admin.py
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'hire_date', 'specialty', 'is_active')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'specialty')
    list_filter = ('is_active', 'specialty')
    ordering = ('-hire_date',)

admin.site.register(Employee, EmployeeAdmin)