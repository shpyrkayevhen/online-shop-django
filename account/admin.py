from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    '''Account model representation and registration in Admin panel.'''
    list_display = ['email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active']   
    readonly_fields = ['password', 'last_login', 'date_joined']
    list_display_links = ['email', 'first_name', 'last_name']
    ordering = ['-date_joined']
