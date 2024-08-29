from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    # English Levels
    LEVEL_CHOICE = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2')
        ]
    
    # User auth
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profile")
    
    # User type
    type_of_user = models.CharField(max_length=7, verbose_name="Type of user")
    
    # Personal details
    name = models.CharField(max_length=15, verbose_name="Name")
    last_name = models.CharField(max_length=15, verbose_name="Last Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number", blank=True, null=True)
    country = models.CharField(max_length=15, verbose_name="Country", blank=True, null=True)
    english_level = models.CharField(max_length=2, choices=LEVEL_CHOICE, verbose_name="English Level")

    # Platform details
    plan_subscribed = models.CharField(max_length=10, verbose_name="Plan Subscribed", blank=True, null=True)
    plan_status = models.BooleanField(default=False, verbose_name="Plan Status")
    
    def __str__(self):
        return f"{self.name} {self.last_name}"


