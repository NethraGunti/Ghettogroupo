from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User, UserProfile, Interest


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


class InterestForm(forms.Form):
    interest = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Interest.objects.all())


class UserProfileForm(forms.ModelForm):
    interest = InterestForm()
    class Meta:
        model = UserProfile
        exclude = ['user']
        widgets = {
            'interest': forms.CheckboxSelectMultiple()
        }