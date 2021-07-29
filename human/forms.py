from django import forms
from .models import Humanlog


class PostForm(forms.ModelForm):
    class Meta:
        model = Humanlog
        fields = ['title', 'body']
        widgets ={
            'created_at' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }


