from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UsernameUpdateForm(forms.Form):
    new_username = forms.CharField(max_length=150)

class PasswordUpdateForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class EmailUpdateForm(forms.Form):
    new_email = forms.EmailField()

class FirstNameUpdateForm(forms.Form):
    new_first_name = forms.CharField(max_length=150)

class LastNameUpdateForm(forms.Form):
    new_last_name = forms.CharField(max_length=150)