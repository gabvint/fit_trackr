from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('',views.home,name='home'),
  path('signin/', views.SignIn.as_view(), name='signin'),
  path('accounts/signup/', views.signup, name="signup"),
  path('dashboard/', views.user_dashboard, name="user_dashboard"),
  path('goals/<int:pk>/update', views.SetGoals.as_view(), name="set_goals"),
  path('workouts/create/', views.CreateWorkout.as_view(), name="create_workout"),
  # path('get_workouts/', views.get_workouts_by_muscle_group, name='get_workouts_by_muscle_group'),
  path('meals/create/', views.CreateMeals.as_view(), name="create_meals"),
  path('workoutlog/', views.workout_log, name="workout_log"),
  path('workoutlog/<int:workout_id>/', views.workout_detail, name="workout_detail"),
  path('workoutlog/<int:pk>/update/', views.WorkoutUpdate.as_view(), name="workout_update"),
  path('workoutlog/<int:pk>/delete/', views.WorkoutDelete.as_view(), name="workout_delete"),
  path('meallog/', views.meal_log, name="meal_log"),
  path('meallog/<int:meal_id>/', views.meal_detail, name="meal_detail"),
  path('meallog/<int:pk>/update/', views.MealUpdate.as_view(), name='meal_update'),
  path('meallog/<int:pk>/delete/', views.MealDelete.as_view(), name='meal_delete'), 
  path('profile/<int:pk>/', views.UserProfile.as_view(), name="user_profile"),
  path('profile/<int:pk>/update', views.UserProfileUpdate.as_view(), name="user_update"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)