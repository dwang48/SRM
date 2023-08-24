from django.contrib import admin
from .models import CustomSchema

# @admin.register(CustomSchema)
# class CustomSchemaAdmin(admin.ModelAdmin):
#     list_display = ['name', 'field_name', 'field_type']  # Customize this to display the fields you want in the admin list view
#     # Add any other admin customizations as needed
