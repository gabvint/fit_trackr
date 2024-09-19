from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DeleteView 
from .workout_api import get_workouts

from .models import Workout


class Home(LoginView):
  template_name = 'home.html'
  
  
class CreateWorkout(CreateView):
  model = Workout
  fields = ['muscle_group']
  

class WorkoutList(CreateView):
  model = Workout
  fields = ['name', 'calorie_lost']
  workouts = get_workouts(model.muscle_group)
  
  
  
  
  
  
  


  
