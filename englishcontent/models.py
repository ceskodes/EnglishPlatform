from django.db import models

# Create your models here.
class EnglishContent(models.Model):
    # English Levels
    LEVEL_CHOICE = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2')
        ]
    
    level = models.CharField(max_length=2, choices=LEVEL_CHOICE , verbose_name="English Level")
    title = models.CharField(max_length=100, verbose_name="Grammar title")
    description = models.CharField(max_length=100, verbose_name="Description")
    status = models.BooleanField(default=False, verbose_name="Topic Status")
    