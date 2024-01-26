from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from .forms import SignUpForm, UsernameUpdateForm, PasswordUpdateForm, EmailUpdateForm, FirstNameUpdateForm, LastNameUpdateForm

from django.contrib.auth.decorators import login_required

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form':form})

@login_required
def account_details_view(request):
    user = request.user
    return render(request, 'account_edit/account_details.html', {'user': user})

@login_required
def username_update_view(request):
    if request.method == 'POST':
        form = UsernameUpdateForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            user = request.user
            user.username = new_username
            user.save()
            return redirect('users:account_details')
    else:
        form = UsernameUpdateForm()
    
    return render(request, 'account_edit/username_update.html', {'form': form})

@login_required
def password_update_view(request):
    if request.method == 'POST':
        form = PasswordUpdateForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            user = request.user
            if user.check_password(current_password) and new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Update session with new password
                return redirect('users:account_details')
            else:
                form.add_error('confirm_password', 'Passwords do not match.')
    else:
        form = PasswordUpdateForm()
    
    return render(request, 'account_edit/password_update.html', {'form': form})

@login_required
def email_update_view(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            user = request.user
            user.email = new_email
            user.save()
            return redirect('users:account_details')
    else:
        form = EmailUpdateForm(initial={'new_email': request.user.email})
    
    return render(request, 'account_edit/email_update.html', {'form': form})

@login_required
def first_name_update_view(request):
    if request.method == 'POST':
        form = FirstNameUpdateForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['new_first_name']
            user = request.user
            user.first_name = new_first_name
            user.save()
            return redirect('users:account_details')
    else:
        form = FirstNameUpdateForm(initial={'new_first_name': request.user.first_name})
    
    return render(request, 'account_edit/first_name_update.html', {'form': form})

@login_required
def last_name_update_view(request):
    if request.method == 'POST':
        form = LastNameUpdateForm(request.POST)
        if form.is_valid():
            new_last_name = form.cleaned_data['new_last_name']
            user = request.user
            user.last_name = new_last_name
            user.save()
            return redirect('users:account_details')
    else:
        form = LastNameUpdateForm(initial={'new_last_name': request.user.last_name})
    
    return render(request, 'account_edit/last_name_update.html', {'form': form})