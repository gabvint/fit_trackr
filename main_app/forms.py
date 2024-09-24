from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NewUser, Workout, Meal
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML


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
    fields = ('username', 'first_name', 'last_name', 'email', 'calorie_goal', 'workout_goal')
    
class UserProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = NewUser
        fields = ['first_name', 'last_name', 'username', 'email', 'profile_picture']
        
            
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = NewUser
        fields = ['new_password1', 'new_password2']

    
class WorkoutForm(forms.ModelForm):
  class Meta:
    model = Workout
    fields = ['day', 'muscle_group', 'name', 'sets', 'reps', 'calorie_lost', 'notes']
  
  def __init__(self, *args, **kwargs):
    available_days = kwargs.pop('available_days', None)
    # workout_list = kwargs.pop('workout_list', [])
    # super().__init__(*args, **kwargs)


    super().__init__(*args, **kwargs)
    if available_days is not None:
      self.fields['day'].queryset = available_days
    # self.fields['name'] = forms.ChoiceField(
    #   choices=[('', 'Select a workout')] + [(workout, workout) for workout in workout_list],
    #   required=False
    #   )
  
  
    self.fields['muscle_group'].widget.attrs['placeholder'] = 'Enter muscle group'
    self.fields['name'].widget.attrs['placeholder'] = 'Select a workout'
    self.fields['sets'].widget.attrs['placeholder'] = 'Number of sets'
    self.fields['reps'].widget.attrs['placeholder'] = 'Number of reps'
    self.fields['calorie_lost'].widget.attrs['placeholder'] = 'Calories burned'
    self.fields['notes'].widget.attrs['placeholder'] = 'Additional notes'

    
    self.helper = FormHelper()
    self.helper.form_class = 'w-96 md:w-[450px] mx-auto bg-offWhite p-8 rounded-lg shadow-md mt-12 mb-12 font-questrial'
    self.helper.layout = Layout(
        Field('day'),
        Field('muscle_group'),
        Field('name'),
        Field('sets'),
        Field('reps'),
        Field('calorie_lost'),
        Field('notes'),
        HTML(
          """
           <button type="submit" class="relative mt-4 rounded-md px-5 py-1 overflow-hidden group bg-black text-cream hover:bg-gradient-to-r
                hover:from-black hover:to-grey hover:ring-2 hover:ring-offset-2 hover:ring-grey transition-all ease-out duration-300">
                    <span class='absolute right-0 w-8 h-32 -mt-12 transition-all duration-1000 transform translate-x-12 bg-white 
                    opacity-10 rotate-12 group-hover:-translate-x-40 ease'></span>
                    <span class='relative'>Submit</span>
            </button>
          """
        ),
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
    
    
    
    self.fields['name'].widget.attrs['placeholder'] = 'Enter meal name'
    self.fields['calories'].widget.attrs['placeholder'] = 'Calories gained'
    self.fields['notes'].widget.attrs['placeholder'] = 'Additional notes'

        
    self.helper = FormHelper()
    self.helper.form_class = 'w-96 md:w-[450px] mx-auto bg-offWhite p-8 rounded-lg shadow-md mt-12 mb-12 font-questrial'
    self.helper.layout = Layout(
        Field('name'),
        Field('day'),
        Field('meal'),
        Field('calories'),
        Field('notes'),
        HTML(
          """
           <button type="submit" class="relative mt-4 rounded-md px-5 py-1 overflow-hidden group bg-black text-cream hover:bg-gradient-to-r
                hover:from-black hover:to-grey hover:ring-2 hover:ring-offset-2 hover:ring-grey transition-all ease-out duration-300">
                    <span class='absolute right-0 w-8 h-32 -mt-12 transition-all duration-1000 transform translate-x-12 bg-white 
                    opacity-10 rotate-12 group-hover:-translate-x-40 ease'></span>
                    <span class='relative'>Submit</span>
            </button>
          """
        ),
    )
    

  