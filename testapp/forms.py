from django import forms 
from django.contrib.auth.models import User
from testapp.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',"password",'email','first_name','last_name']