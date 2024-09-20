from django import forms
from django.contrib.auth.models import User
from .models import Project, ProjectStatus, ProjectPriority, Comment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_description', 'projectPriority', 'projectStatus']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class AssignUsersForm(forms.ModelForm):
    assigned_users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Project
        fields = ['assigned_users']