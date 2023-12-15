from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'