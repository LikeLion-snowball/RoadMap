from django import forms
from .models import Human
from .models import Comment

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

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('author_name', 'comment_text')

class HumanUpdate(forms.ModelForm):
    class Meta:
        model = Human
        fields = ['title','body']