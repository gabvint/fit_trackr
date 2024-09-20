from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .workout_api import get_workouts
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Workout, NewUser, Day, Meal
from .forms import WorkoutForm, MealForm



class Home(LoginView):
  template_name = 'home.html'
  
  
class CreateWorkout(CreateView):
  model = Workout
  form_class = WorkoutForm
  
  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    user = self.request.user
    kwargs['available_days'] = Day.objects.filter(user=user)
    muscle_group = self.request.POST.get('muscle_group', None)
    if muscle_group:
        workouts_response = get_workouts(muscle_group)
        if workouts_response.status_code == 200:
            data = workouts_response.json()
            workout_list = [item['WorkOut'] for item in data if 'Muscles' in item]
            kwargs['workout_list'] = workout_list
        else:
            kwargs['workout_list'] = []
    return kwargs

def get_workouts_by_muscle_group(request):
    muscle_group = request.GET.get('muscle_group')
    workouts_response = get_workouts(muscle_group)
    if workouts_response.status_code == 200:
        data = workouts_response.json()
        workout_list = [item['WorkOut'] for item in data if 'Muscles' in item]
        return JsonResponse({'workouts': workout_list})
    return JsonResponse({'workouts': []})

class CreateMeals(CreateView):
    model = Meal
    form_class = MealForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs['available_days'] = Day.objects.filter(user=user)
        return kwargs

class WorkoutList(CreateView):
    model = Workout
    fields = ['name', 'calorie_lost']
    success_url = reverse_lazy('workout_list')  

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        muscle_group = self.request.GET.get('muscle_group', 'default_muscle_group')  
        workouts_response = get_workouts(muscle_group)
        
        if workouts_response.status_code == 200:
            data = workouts_response.json()
            workout_list = [item['WorkOut'] for item in data if 'Muscles' in item]
        else:
            workout_list = []
            
            
        kwargs['initial'] = {'name': workout_list}
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

class SetGoals(UpdateView):
    model = NewUser
    fields = ['workout_goal', 'calorie_goal']

def user_dashboard(request):
  return render(request, 'dashboard.html')

def meal_log(request):
  return render(request, 'meal_log.html')

def workout_log(request):
    user = request.user
    workouts = Workout.objects.filter(day__user=user)
    return render(request, 'workout_log.html', {'workouts': workouts})
    
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


  
