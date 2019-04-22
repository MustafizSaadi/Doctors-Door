from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Person
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     FirstName = forms.charField(max=50)
#
#
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2','FirstName']

class UserForm(forms.ModelForm):
    password1 = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['gender','registration_number','hall_name','department_name','admission_year','phone_number','blood_group','date_of_birth']