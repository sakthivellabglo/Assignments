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