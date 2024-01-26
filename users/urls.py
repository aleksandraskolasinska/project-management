from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('account/', views.account_details_view, name='account_details'),
    path('account/username/update/', views.username_update_view, name='username_update'),
    path('account/password/update/', views.password_update_view, name='password_update'),
    path('account/email/update/', views.email_update_view, name='email_update'),
    path('account/first_name/update/', views.first_name_update_view, name='first_name_update'),
    path('account/last_name/update/', views.last_name_update_view, name='last_name_update'),
]
