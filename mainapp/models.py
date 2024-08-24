from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.TextField(max_length=15)
    last_name = models.TextField(max_length=15)
    email = models.TextField(max_length=30)
    phone_number = models.TextField(max_length=15)
    country = models.TextField(max_length=15)
    english_level = models.TextField(max_length=2)
    
    def __str__(self):
        return self.name