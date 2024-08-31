from django.db import models

# Create your models here.
class A1Content(models.Model):
    # Relación 1:1 con el título de EnglishContent
    title = models.CharField(max_length=100, verbose_name="Topic Title")
    pdf_files = models.FileField(upload_to='pdfs/', verbose_name="PDF File")
    
    def __str__(self):
        return self.title
    