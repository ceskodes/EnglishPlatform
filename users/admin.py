from django.contrib import admin
from .models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    model = Person
    
    # Display if status is activated or not
    list_display = ['user', 'english_level', 'plan_status', 'plan_subscribed']
    
    # Search bar
    search_fields = ['user']
    
admin.site.register(Person, PersonAdmin)