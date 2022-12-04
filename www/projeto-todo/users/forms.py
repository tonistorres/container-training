from django import forms
from .models import User


class UserForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter title task",
                "max_length": 40,
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "exemplo@xxxx.com",
                "max_length": 40,
            }
        )
    )

    celular = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "(xx) 9xxxx-xxxx",
                "max_length": 14,
            }
        )
    )

    class Meta:
        model = User
        fields = ("nome", "celular", "email")
