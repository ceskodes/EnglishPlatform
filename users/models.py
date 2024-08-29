from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    # User auth
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person')
    
    # Personal details
    name = models.CharField(max_length=15, verbose_name="Name")
    last_name = models.CharField(max_length=15, verbose_name="Last Name")
    email = models.EmailField(max_length=30, verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number", blank=True, null=True)
    country = models.CharField(max_length=15, verbose_name="Country", blank=True, null=True)
    english_level = models.CharField(max_length=2, verbose_name="English Level", blank=True, null=True)

    # Platform details
    plan_subscribed = models.CharField(max_length=1, verbose_name="Plan Subscribed", blank=True, null=True)
    plan_status = models.BooleanField(default=False, verbose_name="Plan Status")


    def __str__(self):
        return f"{self.name} {self.last_name}"
