from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Q_Comment, Qna

class PostForm(forms.ModelForm):
    class Meta:
        model = Qna
        fields = ['title', 'body']
        widgets = {
        'title': forms.TextInput(
            attrs={'placeholder': '제목을 입력하세요'}
            ),
        'body': forms.Textarea(
            attrs={'placeholder': '질문을 입력하세요'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Q_Comment
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