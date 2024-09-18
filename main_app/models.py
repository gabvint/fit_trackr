from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    workout_goal = models.IntegerField(null=True, blank=True)
    calorie_goal = models.IntegerField(null=True, blank=True)   
    