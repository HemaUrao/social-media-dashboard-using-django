

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .twitter_api import get_user_tweets
from .models import SocialAccount

def home_redirect_view(request):
    """
    Redirects authenticated users to the dashboard and unauthenticated
    users to the registration page.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('register')

def register_view(request):
    """
    Handles user registration. If the user is already authenticated,
    they are redirected to the dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, "dashboard/register.html", {"form": form})

@login_required
def dashboard_view(request):
    """
    Displays the user's dashboard. Fetches social account information
    and tweets.
    """
    social_accounts = SocialAccount.objects.filter(user=request.user)
    
   
    tweets = []
    twitter_account = social_accounts.filter(platform='twitter').first()
    if twitter_account:
        tweets = get_user_tweets(screen_name=twitter_account.account_username)

    context = {
        'socials': social_accounts,
        'tweets': tweets
    }
    
    return render(request, "dashboard/dashboard.html", context)
