from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .workout_api import get_workouts
import json
from django.urls import reverse_lazy
from .models import Workout, NewUser


class Home(LoginView):
  template_name = 'home.html'
  
  
class CreateWorkout(CreateView):
  model = Workout
  fields = ['muscle_group']
  
  

class WorkoutList(CreateView):
    model = Workout
    fields = ['name', 'calorie_lost']
    success_url = reverse_lazy('workout_list')  # Redirect after form submission

    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
        
        # Retrieve muscle group from request or some source
        muscle_group = self.request.GET.get('muscle_group', 'default_muscle_group')  # Replace with actual default or passed value
        
        # Fetch workouts from API
        workouts_response = get_workouts(muscle_group)
        
        if workouts_response.status_code == 200:
            data = workouts_response.json()
            workout_list = [item['WorkOut'] for item in data if 'Muscles' in item]
        else:
            workout_list = []

        # Pass the workout list to the form as a keyword argument
        kwargs['initial'] = {'name': workout_list}
        return kwargs

    def form_valid(self, form):
        # Override form_valid to handle form submission logic
        # You might want to add custom logic here or handle the form differently
        return super().form_valid(form)

class SetGoals(UpdateView):
    model = NewUser
    fields = ['workout_goal', 'calorie_goal']

def user_dashboard(request):
  return render(request, 'dashboard.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
        else:
            error_message = 'Invalid sign up - try again'

    form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


  
