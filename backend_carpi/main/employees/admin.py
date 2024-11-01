# employees/admin.py

from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'hire_date', 'specialty', 'is_active', 'days_since_hired')
    search_fields = ('user__username', 'specialty')
    list_filter = ('is_active', 'specialty')
    ordering = ('hire_date',)

    def days_since_hired(self, obj):
        return obj.days_since_hired()
    days_since_hired.short_description = 'Días desde la contratación'

admin.site.register(Employee, EmployeeAdmin)