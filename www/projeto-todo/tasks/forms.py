# https://www.youtube.com/watch?v=la_MTnWEBMM&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=11
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    error_css_class = "error-field"
    required_css_class = "required-field"

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control text-white text-center",
                "max_length": "100",
                "placeholder": "Enter title   task",
            }
        )
    )

    resumetask = forms.CharField(widget=forms.Textarea(attrs={"cols": 40, "rows": 10}))

    class Meta:
        model = Task
        fields = ("title", "resumetask")
