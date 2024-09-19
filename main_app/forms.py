from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from.models import NewUser, Workout

class CustomUserCreationForm(UserCreationForm):
  username = forms.CharField(max_length=150)
  first_name = forms.CharField(max_length=150)
  last_name = forms.CharField(max_length=150)
  email = forms.EmailField(max_length=150)
  calorie_goal=forms.IntegerField()
  workout_goal=forms.IntegerField()
  class Meta:
    model = NewUser
    fields = ('username', 'first_name', 'last_name', 'email', 'calorie_goal', 'workout_goal', 'password1', 'password2')
    
    
class CustomUserChangeForm(UserChangeForm):
  username = forms.CharField(max_length=150)
  first_name = forms.CharField(max_length=150)
  last_name = forms.CharField(max_length=150)
  email = forms.EmailField(max_length=150)
  calorie_goal=forms.IntegerField()
  workout_goal=forms.IntegerField()
  class Meta:
    model = NewUser
    fields = ('username', 'first_name', 'last_name', 'email', 'calorie_goal', 'workout_goal')
    
    
class WorkoutForm(forms.ModelForm):
  class Meta:
    model = Workout
    fields = ['name', 'day', 'muscle_group']
  
  def __init__(self, *args, **kwargs):
    available_days = kwargs.pop('available_days', None)
    super().__init__(*args, **kwargs)
    if available_days is not None:
      self.fields['day'].queryset = available_days
  