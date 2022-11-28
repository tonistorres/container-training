# https://www.youtube.com/watch?v=la_MTnWEBMM&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=11
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "resumetask")
