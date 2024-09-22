from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NewUser, Workout, Meal
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
            'placeholder': 'Password'
        })
    )

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
            'placeholder': 'Username'
        })
    )
    first_name = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        max_length=150,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
            'placeholder': 'Email'
        })
    )
    # calorie_goal = forms.IntegerField(
    #     label='',
    #     widget=forms.NumberInput(attrs={
    #         'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
    #         'placeholder': 'Calorie Goal'
    #     })
    # )
    # workout_goal = forms.IntegerField(
    #     label='',
    #     widget=forms.NumberInput(attrs={
    #         'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
    #         'placeholder': 'Workout Goal'
    #     })
    # )
    # meal_goal = forms.IntegerField(
    #     label='',
    #     widget=forms.NumberInput(attrs={
    #         'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
    #         'placeholder': 'Meal Goal'
    #     })
    # )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-darkerSage',
            'placeholder': 'Confirm Password'
        })
    )
    class Meta:
        model = NewUser
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    
    
class CustomUserChangeForm(UserChangeForm):
  username = forms.CharField(max_length=150)
  first_name = forms.CharField(max_length=150)
  last_name = forms.CharField(max_length=150)
  email = forms.EmailField(max_length=150)
  calorie_goal=forms.IntegerField()
  workout_goal=forms.IntegerField()
  class Meta:
    model = NewUser
    fields = ('username', 'first_name', 'last_name', 'email', 'calorie_goal', 'workout_goal', 'meal_goal')
    
    
class WorkoutForm(forms.ModelForm):
  class Meta:
    model = Workout
    fields = ['day', 'muscle_group', 'name', 'sets', 'reps', 'calorie_lost', 'notes']
  
  def __init__(self, *args, **kwargs):
    available_days = kwargs.pop('available_days', None)
    workout_list = kwargs.pop('workout_list', [])
    super().__init__(*args, **kwargs)


    super().__init__(*args, **kwargs)
    if available_days is not None:
      self.fields['day'].queryset = available_days
    self.fields['name'] = forms.ChoiceField(
      choices=[('', 'Select a workout')] + [(workout, workout) for workout in workout_list],
      required=False
      )
    
  def clean_name(self):
        """Allow the 'name' field to accept dynamically added values, and make it optional for specific muscle groups."""
        name = self.cleaned_data.get('name')
        muscle_group = self.cleaned_data.get('muscle_group')
        if muscle_group == "Warm":
            return name
        if not name:
            raise forms.ValidationError("This field is required.")
        return name

  
class MealForm(forms.ModelForm):
  class Meta: 
    model = Meal
    fields = ['name', 'meal', 'day', 'calories', 'notes']
    
  def __init__(self, *args, **kwargs):
    available_days = kwargs.pop('available_days', None)
    super().__init__(*args, **kwargs)
    if available_days is not None:
      self.fields['day'].queryset = available_days
    # self.fields['name'].widget.attrs.update({
    #         'id': 'food-search',
    #         'placeholder': 'Search for a food...',
    #         'autocomplete': 'off'
    #     })

  