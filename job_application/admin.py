from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):  # ModelAdmin = Class designed to create admin interfaces
    list_display = ("first_name", "last_name", "email", "date", "occupation")  # Makes admin table with the listed columns
    search_fields = ("first_name", "last_name", "email")  # Makes a search bar to look for the listed fields
    list_filter = ("date", "occupation")  # Makes a filter table for the listed categories
    ordering = ("first_name", )  # Display names in order
    readonly_fields = ("occupation", )  # Makes a data category read-only, unchangeable by admin

admin.site.register(Form, FormAdmin)  # Register function expects a class to register it with the admin interface
