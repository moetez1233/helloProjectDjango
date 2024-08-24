from django import forms
from playground.models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'email', 'message']
