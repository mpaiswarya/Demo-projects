from django import forms
from .models import home

class homeforms(forms.ModelForm):
    class Meta:
        model=home
        fields=['name','place','price','img']