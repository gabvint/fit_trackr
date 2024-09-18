from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

# Create your models here.

    
class NewUser(AbstractUser):
    workout_goal = models.IntegerField(null=True, blank=True)
    calorie_goal = models.IntegerField(null=True, blank=True)
    
class Day(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    
    
class Meal(models.Model):
    name = models.CharField()
    meal = models.CharField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    