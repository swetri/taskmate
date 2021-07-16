from django import forms
from django.db.models import fields
from .models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']



        

