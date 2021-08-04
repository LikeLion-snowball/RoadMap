from django import forms
from .models import Humanlog, Comment


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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': '댓글을 작성해주세요',
                'style': 'font-size: 1.1rem; width: calc(100% - 8rem); height: 3rem; border-radius: 10px; border: 1px solid gray; padding: 1rem;'
            }),
        }
        labels = {
            'content': ''
        }