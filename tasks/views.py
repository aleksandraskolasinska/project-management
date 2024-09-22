from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.views import generic
from django.urls import reverse, reverse_lazy
# from django.db.models import Q

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required


from .models import Project, ProjectStatus
from .forms import ProjectForm, CommentForm, AssignUsersForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def project_list(request):
    if request.user.is_superuser:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(created_by=request.user) | Project.objects.filter(assigned_users=request.user)

    if not projects:
        no_projects_message = "You haven't created or been assigned to any projects yet."
        return render(request, 'tasks/project_list.html', {'no_projects_message':no_projects_message})

    return render(request, 'tasks/project_list.html', {
        'projects': projects,
    })

    
    # return render(request, 'tasks/project_list.html', {'projects': projects})


from django.forms.models import model_to_dict

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    comments = project.comments.all()
    history = project.history.all()


    if not (request.user.is_superuser or request.user.groups.filter(name="Admin").exists() or request.user in project.assigned_users.all()):
        return HttpResponseForbidden("You are not authorized to view this page.")

    if request.method == 'POST' and 'comment_submit' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect('tasks:project_detail', project_id=project_id)
    else:
        comment_form = CommentForm()

    changes = []
    for entry in history:

        diff = {}
        prev_record = entry.prev_record
        if prev_record:
            if prev_record.project_title != entry.project_title:
                diff['title'] = {
                    'old': prev_record.project_title,
                    'new': entry.project_title
                }
            if prev_record.project_description != entry.project_description:
                diff['description'] = {
                    'old': prev_record.project_description,
                    'new': entry.project_description
                }
            if prev_record.projectStatus != entry.projectStatus:
                diff['status'] = {
                    'old': prev_record.projectStatus,
                    'new': entry.projectStatus
                }
            if prev_record.projectPriority != entry.projectPriority:
                diff['priority'] = {
                    'old': prev_record.projectPriority,
                    'new': entry.projectPriority
                }
            if diff:
                changes.append({
                    'date': entry.history_date,
                    'user': entry.history_user,  
                    'type': entry.history_type,
                    'diff': diff
                })


    return render(request, 'tasks/project_detail.html', {
        'project': project,
        'comments': comments,
        'comment_form': comment_form,
        'changes': changes,
    })

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

    if not (request.user.is_superuser or request.user.groups.filter(name="Admin").exists() or request.user in project.assigned_users.all()):
        return HttpResponseForbidden("You are not authorized to view this page.")

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

    if not (request.user.is_superuser or request.user.groups.filter(name="Admin").exists() or request.user in project.assigned_users.all()):
        return HttpResponseForbidden("You are not authorized to view this page.")

    if request.method == 'POST':
        project.delete()
        return redirect('tasks:project_list')

    return render(request, 'tasks/delete_project.html', {'project': project})

@login_required
def assign_users(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = AssignUsersForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('tasks:project_detail', project_id=project_id)
    else:
        form = AssignUsersForm(instance=project)

    return render(request, 'tasks/assign_users.html', {'form': form, 'project': project})