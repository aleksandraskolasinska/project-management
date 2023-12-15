from django.db import models
import datetime 

from django.utils import timezone
from django.contrib.auth.models import User, Permission
# from simple_history.models import HistoricalRecords

# Create your models here.

class ProjectStatus(models.TextChoices):
    to_do = 'To do'
    in_progress = 'In progress'
    done = 'Done'

class Project(models.Model):
    # project_id = 
    project_title = models.CharField(max_length=150)
    project_description = models.TextField()
    start_date = models.DateTimeField('date created', auto_now_add = True)
    update_date = models.DateTimeField('date of update', auto_now = True)
    end_date = models.DateTimeField('date of completion', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name="created_projects")
    last_edited_by  = models.ForeignKey(User, on_delete=models.CASCADE)
    projectStatus = models.CharField(max_length=20, choices=ProjectStatus.choices, default=ProjectStatus.to_do)

    # history = HistoricalRecords()
# class Task(model.Model):
#     task_name
#     task_description
#     project_id      
