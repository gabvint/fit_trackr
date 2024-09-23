from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .api import get_workouts
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Workout, NewUser, Day, Meal, MEALS
from .forms import WorkoutForm, MealForm, CustomAuthenticationForm
from datetime import datetime
from django.db.models import Count


from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
  return render(request, 'home.html')

class SignIn(LoginView):
  template_name = 'signin.html'
  authentication_form = CustomAuthenticationForm
  
class CreateWorkout(CreateView, LoginRequiredMixin):

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


class CreateMeals(CreateView, LoginRequiredMixin):
    model = Meal
    form_class = MealForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs['available_days'] = Day.objects.filter(user=user)
        return kwargs
    
# def search_food(request):
#     food_search = request.GET.get('q', None)
    
#     if not food_search:
#         return JsonResponse([], safe=False)

#     food_search_response = get_foods(food_search)
    
#     if food_search_response.status_code == 200:
#         data = food_search_response.json()
#         food_items = [
#             {
#                 "name": item['description'],
#                 "calories": next((nutrient['value'] for nutrient in item['foodNutrients'] if nutrient['nutrientName'] == "Calories"), 0)
#             }
#             for item in data.get('foods', [])
#         ]
#         return JsonResponse(food_items, safe=False)
#     else:
#         print(f"Error fetching foods: {food_search_response.status_code}")
#         return JsonResponse([], safe=False)


class WorkoutList(CreateView, LoginRequiredMixin):
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

class WorkoutUpdate(UpdateView, LoginRequiredMixin):
    model = Workout
    form_class = WorkoutForm
    
class WorkoutDelete(DeleteView, LoginRequiredMixin):
    model = Workout
    success_url = '/workoutlog/'

class SetGoals(UpdateView, LoginRequiredMixin):
    model = NewUser
    fields = ['workout_goal', 'calorie_goal']

class MealUpdate(UpdateView, LoginRequiredMixin):
    model = Meal
    form_class = MealForm
    
class MealDelete(DeleteView, LoginRequiredMixin):
    model = Meal
    success_url = '/meallog/'

@login_required
def user_dashboard(request):
  selected_date = request.GET.get('workout_date', None)
  user = request.user
  calorie_goal = user.calorie_goal or 0
  workout_goal = user.workout_goal  or 0
  

  if selected_date:
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        recent_workouts = Workout.objects.filter(day__date=selected_date, day__user=user).order_by('-day')[:2]
        recent_meals = Meal.objects.filter(day__date=selected_date, day__user=user).order_by('-id')[:2]
        todays_meals = Meal.objects.filter(day__date=selected_date, day__user=user)
        todays_workouts = Workout.objects.filter(day__date=selected_date, day__user=user)
  else: 
        selected_date = datetime.today().date()
        recent_workouts = Workout.objects.filter(day__date=selected_date, day__user=user).order_by('-day')[:2]
        recent_meals = Meal.objects.filter(day__date=selected_date, day__user=user).order_by('-id')[:2]
        todays_meals = Meal.objects.filter(day__date=selected_date, day__user=user)
        todays_workouts = Workout.objects.filter(day__date=selected_date, day__user=user)
        

  total_meal_calories = todays_meals.aggregate(total_calories=Sum('calories')).get('total_calories') or 0
  total_workout_calories = todays_workouts.aggregate(total_calorie_lost=Sum('calorie_lost')).get('total_calorie_lost') or 0
  net_calories = calorie_goal - total_meal_calories + total_workout_calories
  todays_meal_count = todays_meals.count()
  todays_workout_count = todays_workouts.count()
  meal_counts = Meal.objects.filter(day__user=user, day__date=selected_date) \
    .values('meal') \
    .annotate(count=Count('id'))
  meal_labels = {key: value for key, value in MEALS}
  labels = [meal_labels[meal['meal']] for meal in meal_counts]
  values = [meal['count'] for meal in meal_counts]


  return render(request, 'dashboard.html', {
        'recent_meals': recent_meals, 
        'recent_workouts': recent_workouts, 
        'total_meal_calories': total_meal_calories,     
        'total_workout_calories': total_workout_calories,
        'net_calories': net_calories,
        'calorie_goal': calorie_goal,
        'workout_goal': workout_goal,
        'todays_meal_count': todays_meal_count ,
        'todays_workout_count': todays_workout_count,
        'selected_date': selected_date,
        'labels': labels,
        'values': values,
        })

@login_required
def meal_log(request):
   user = request.user
   meals = Meal.objects.filter(day__user=user).order_by('-day')
   return render(request, 'meal_log.html', { 'meals': meals })

@login_required
def meal_detail(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    return render(request, 'meal_detail.html', { 'meal': meal })

@login_required
def workout_log(request):
    user = request.user
    workouts = Workout.objects.filter(day__user=user).order_by('-day')
    return render(request, 'workout_log.html', { 'workouts': workouts })

@login_required
def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workout_detail.html', { 'workout': workout })
    
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


