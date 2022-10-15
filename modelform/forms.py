# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import *
 
# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = stu
        fields = "__all__"
class markForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = mark
        fields = ["student","subject","mark",]

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 
 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'email']
 
 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']