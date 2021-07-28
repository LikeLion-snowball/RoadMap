from django import forms
from django.forms import widgets
from .models import Activity, Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_start', 'project_end', 'project_detail', 'project_github']
        widgets ={
            'project_start' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'date'
                }
            ),
            'project_end' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_name', 'activity_start', 'activity_end']
        widgets ={
            'activity_start' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'date'
                }
            ),
            'activity_end' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }