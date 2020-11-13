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

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['image','age','organization','occupation']


class InterestForm(forms.ModelForm):
    INTERESTS = [
    ("Agriculture", "Agriculture"),
    ("Arts and Entertainment", "Arts and Entertainment"),
    ("Education", "Education"),
    ("Food", "Food"),
    ("Hardware and Automobiles", "Hardware and Automobiles"),
    ("Healthcare and Medicine", "Healthcare and Medicine"),
    ("Law and Enforcement", "Law and Enforcement"),
    ("Sales and Management", "Sales and Management"),
    ("Science and Technology", "Science and Technology"),
]
    interest = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=INTERESTS,)
    class Meta:
        model = Interest
        fields = ['interest']