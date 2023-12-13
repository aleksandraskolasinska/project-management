from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from .models import Project

# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ('project_title', 'created_by', 'projectStatus', 'start_date', 'update_date')
    readonly_fields = ['created_by', 'start_date', 'update_date']


    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
  
    def get_readonly_fields(self, request, obj=None):
        if obj:
            # Check if the user is staff/admin
            if request.user.is_staff or request.user.is_superuser:
                return self.readonly_fields + ['project_description']
        return self.readonly_fields