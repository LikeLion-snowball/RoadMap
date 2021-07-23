from django import forms
from .models import Human

class PostForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ['title', 'body', 'pub_date']
        widgets ={
            'pub_date' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }