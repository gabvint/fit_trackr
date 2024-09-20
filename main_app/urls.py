from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('accounts/signup/', views.signup, name="signup"),
  path('dashboard/', views.user_dashboard, name="user_dashboard"),
  path('goals/<int:pk>/update', views.SetGoals.as_view(), name="set_goals"),
  path('workouts/create/', views.CreateWorkout.as_view(), name="create_workout"),
  path('get_workouts/', views.get_workouts_by_muscle_group, name='get_workouts_by_muscle_group'),
  path('meals/create/', views.CreateMeals.as_view(), name="create_meals"),
  path('meals/search/', views.search_food, name='search_food'),
  path('workoutlog/', views.workout_log, name="workout_log"),
  path('workoutlog/<int:workout_id>/', views.workout_detail, name="workout_detail"),
  path('meallog/', views.meal_log, name="meal_log"),
  path('meallog/<int:meal_id>/', views.meal_info, name="meal_info"),
]