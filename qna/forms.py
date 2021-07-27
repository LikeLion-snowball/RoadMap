from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Qna

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