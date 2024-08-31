from django.contrib import admin
from .models import A1Content

# Register your models here.
class A1ContentAdmin(admin.ModelAdmin):
    model = A1Content
    
    # Display if status is activated or not
    list_display = ['title', 'pdf_files']
    
admin.site.register(A1Content, A1ContentAdmin)