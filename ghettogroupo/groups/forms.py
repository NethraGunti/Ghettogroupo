from django import forms

from groups.models import Group, GROUPS

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['type', 'name', 'description']
        widgets={
            'type': forms.Select(attrs={'class':'form-group form-control', 'placeholder':'group type'}),
            'name':forms.TextInput(attrs={'class':'form-group form-control', 'placeholder': 'group title'}),
            'description':forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'group description'}),
        }

    def __init__(self, types=None, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        self.fields['type'].choices = types


    def get_cleaned_data(self, post_data):
        converted_post_data = dict(post_data)
        converted_post_data.pop('csrfmiddlewaretoken')
        return converted_post_data


class JoinGroupForm(forms.Form):
    group_code = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-group form-control',
                'placeholder':'group code'
            }
        )
    )
    