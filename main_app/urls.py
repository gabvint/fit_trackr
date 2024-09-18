from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('workout/create', views.CreateWorkout.as_view(), name="create_workout"),
  path('workout/<str:muscle_group>/', views.WorkoutList.as_view(), name="workout_list"),
]