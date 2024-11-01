# capital/admin.py
from django.contrib import admin
from .models import Capital

class CapitalAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'description')
    list_filter = ('date',)
    search_fields = ('description',)

admin.site.register(Capital, CapitalAdmin)