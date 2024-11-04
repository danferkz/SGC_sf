# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 

class CustomUserAdmin(UserAdmin):
    model = CustomUser 
    list_display = ('username', 'email', 'first_name', 'last_name', 'dni', 'is_client', 'is_staff', 'is_active')
    list_filter = ('is_client', 'is_staff', 'is_active', 'gender')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('dni', 'address', 'phone', 'gender', 'is_client')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('dni', 'address', 'phone', 'gender', 'is_client')}),
    )
    search_fields = ('username', 'email', 'dni', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)