from django.forms import ModelForm
from .models import Movie, Comment
from django import forms

class MovieForm(ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty")

    class Meta:
        model = Movie 
        exclude = ('created_at',)

    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("Honeypot should be empty")
        return honeypot

class CommentForm(ModelForm):
     
    class Meta:
        model = Comment
        exclude = ('created_at',)
