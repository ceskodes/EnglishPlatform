from django.contrib import admin
from .models import EnglishContent

# Register your models here.
class EnglishContentAdmin(admin.ModelAdmin):
    model = EnglishContent
    
    # Display if status is activated or not
    list_display = ['title', 'level', 'status']
    
    # Search bar
    search_fields = ['title', 'level']
    
admin.site.register(EnglishContent, EnglishContentAdmin)
