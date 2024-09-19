from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('dashboard/', views.user_dashboard, name="user_dashboard"),
  # path('goals/', views.GoalsList.as_view(), name="goals_index"),
  path('goals/<int:pk>/update', views.SetGoals.as_view(), name="set_goals"),
  path('workouts/create/', views.CreateWorkout.as_view(), name="create_workout"),
  path('accounts/signup/', views.signup, name="signup"),
]