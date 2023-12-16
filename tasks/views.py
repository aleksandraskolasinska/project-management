from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required

from .models import Project, ProjectStatus
from .forms import ProjectForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'tasks/project_detail.html', {'project': project})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.last_edited_by = request.user
            project.save()

            if project.projectStatus == ProjectStatus.done:
                project.end_date = timezone.now()
                project.save()

            return redirect('tasks:project_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/create_project.html', {'form': form})

@login_required
def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.last_edited_by = request.user
            project.save()
            return redirect('tasks:project_detail', project_id=project_id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'tasks/update_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('tasks:project_list')

    return render(request, 'tasks/delete_project.html', {'project': project})
