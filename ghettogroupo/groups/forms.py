from django import forms

from groups.models import Group

class GroupCreationForm(forms.ModelForm):
    
    class Meta:
        model = Group
        fields = ['type', 'name', 'description']
        widgets={
            'type': forms.Select(attrs={'class':'form-group form-control', 'placeholder':'group type'}),
            'name':forms.TextInput(attrs={'class':'form-group form-control', 'placeholder': 'group title'}),
            'description':forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'group description'}),
        }