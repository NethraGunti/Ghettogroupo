from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input2', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input2', 'placeholder': 'confirm password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'fullName', 'password1', 'password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'input2', 'placeholder':'username'}),
            'email':forms.EmailInput(attrs={'class':'input2', 'placeholder': 'email'}),
            'fullName':forms.TextInput(attrs={'class':'input2', 'placeholder':'full name'}),
        }