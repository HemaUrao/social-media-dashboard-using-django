# dashboard/admin.py

from django.contrib import admin
from .models import SocialAccount

# Register the SocialAccount model to make it accessible in the Django admin panel
@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'account_username', 'created_at')
    list_filter = ('platform', 'created_at')
    search_fields = ('user__username', 'account_username')
