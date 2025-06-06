
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, dashboard_view, home_redirect_view

urlpatterns = [
    path('', home_redirect_view, name='home_redirect'),
    
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('dashboard/', dashboard_view, name='dashboard'),
]
