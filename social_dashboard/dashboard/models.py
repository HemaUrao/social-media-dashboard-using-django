
from django.db import models
from django.contrib.auth.models import User

class SocialAccount(models.Model):
    """
    Represents a social media account linked to a user.
    """
    PLATFORM_CHOICES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_accounts')
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    account_username = models.CharField(max_length=100)
    access_token = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s {self.platform.capitalize()} Account"
