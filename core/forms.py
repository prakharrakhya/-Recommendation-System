#models -> forms

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms.widgets import PasswordInput , TextInput

#register User
class RegisterForm(UserCreationForm):
    
    class Meta:
        
        model = User #default model User
        fields = ['username' , 'email' 
                  , 'password1' , 'password2']

#Authenticate User
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



