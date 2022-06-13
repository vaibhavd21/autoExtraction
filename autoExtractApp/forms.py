from django import forms
from .models import data


class MyModelForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ['host','product','startDate','endDate']