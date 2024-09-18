from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets, 
#         (
#             'User Goals', 
#             {
#                 'fields': (
#                     'workout_goal', 
#                     'calorie_goal', 
#                 )
#             }
#         )
#     )
# admin.site.register(NewUser, CustomUserAdmin)


# fields = list(UserAdmin.fieldsets)
# fields[1] =  ('Personal Info', {'fields' : ('first_name', 'last_name', 'email', 'workout_goal', 'calorie_goal')})
# UserAdmin.fieldsets = tuple(fields)
# admin.site.register(NewUser, UserAdmin)

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = NewUser
  list_display = ['username', 'first_name', 'last_name', 'email', 'calorie_goal', 'workout_goal']
  
  fieldsets = list(UserAdmin.fieldsets)
  fieldsets[1] =  ('Personal Info', {'fields' : ('first_name', 'last_name', 'email', 'workout_goal', 'calorie_goal')})
  fieldsets = tuple(fieldsets)
  
admin.site.register(NewUser, CustomUserAdmin)
