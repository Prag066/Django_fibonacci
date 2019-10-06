from django import forms
from .models import Fib_data


class Fib_data_Form(forms.ModelForm):
    class Meta:
        model = Fib_data
        fields = ['number',]
