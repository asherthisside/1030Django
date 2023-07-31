from django import forms 
from .models import Employee_manager

field_choices = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('not specified', 'Not Specified'),
]

class LoginForm(forms.Form):
    name = forms.CharField(max_length=55, label="Enter you name here")
    password = forms.CharField(max_length=20)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=field_choices)


class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = Employee_manager
        fields = ['name', 'deptt', 'salary']  