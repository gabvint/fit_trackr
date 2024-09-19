from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('workout/create/', views.CreateWorkout.as_view(), name="create_workout"),
  path('workout/<int:workout_id>/<str:muscle_group>/', views.WorkoutList.as_view(), name="workout_list"),
  path('dashboard/', views.user_dashboard, name="user_dashboard"),
  # path('goals/', views.GoalsList.as_view(), name="goals_index"),
  path('goals/<int:pk>/update', views.SetGoals.as_view(), name="set_goals"),
  path('accounts/signup/', views.signup, name="signup"),
]