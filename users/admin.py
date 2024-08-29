from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    
    # Display if status is activated or not
    list_display = ['user', 'english_level', 'plan_status', 'plan_subscribed']
    
    # Search bar
    search_fields = ['user']
    
admin.site.register(UserProfile, UserProfileAdmin)