from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser, Day, Meal, Workout
from .forms import CustomUserChangeForm, CustomUserCreationForm



class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = NewUser
  list_display = ['username', 'first_name', 'last_name', 'email', 'calorie_goal', 'workout_goal', 'profile_picture']
  
  fieldsets = list(UserAdmin.fieldsets)
  fieldsets[1] =  ('Personal Info', {'fields' : ('first_name', 'last_name', 'email', 'workout_goal', 'calorie_goal', 'profile_picture')})
  fieldsets = tuple(fieldsets)
  
admin.site.register(NewUser, CustomUserAdmin)

admin.site.register(Day)
admin.site.register(Meal)
admin.site.register(Workout)


