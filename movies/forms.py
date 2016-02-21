from django.forms import ModelForm
from .models import Movie 
from django import forms

class MovieForm(ModelForm):
    class Meta:
        model = Movie 

        exclude = ('created_at',)
