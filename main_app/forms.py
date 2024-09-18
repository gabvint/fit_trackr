from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from.models import NewUser

class CustomUserCreationForm(UserCreationForm):
  # username = forms.CharField(max_length=150)
  # first_name = forms.CharField(max_length=150)
  # last_name = forms.CharField(max_length=150)
  # email = forms.EmailField(max_length=150)
  # password1=forms.CharField(widget=forms.PasswordInput)
  # password2=forms.CharField(widget=forms.PasswordInput)
  # calorie_goal=forms.IntegerField()
  # workout_goal=forms.IntegerField()
  class Meta:
    model = NewUser
    fields = ('username', 'first_name', 'last_name', 'email', 'calorie_goal', 'workout_goal')
    
    
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = NewUser
    fields = ('username', 'first_name', 'last_name', 'email', 'calorie_goal', 'workout_goal')