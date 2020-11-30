from collections import defaultdict

from django import forms
from django.forms.utils import ErrorDict


from groups.models import Membership
from tasks.models import Task

class CreateTaskForm(forms.ModelForm):
    subgroups = forms.MultipleChoiceField(label='Assign To', widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Task
        include = ['subgroups']
        exclude = ['assigned_by']
    def __init__(self, subgroups=None, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        self.fields['subgroups'].choices = subgroups
        self.fields['subgroups'].help_text = 'default is full group. choose to assign to specific people'

    
    def get_cleaned_data(self, post_data):
        converted_post_data = dict(post_data)
        converted_post_data.pop('csrfmiddlewaretoken')
        return converted_post_data
# class CreateTaskForm(forms.ModelForm):
#     task_title = forms.CharField(label='Title', max_length=100, required=True)
#     task_desc = forms.CharField(label='Description', max_length=500, required=True)
#     deadline = forms.DateTimeField(label='Deadline', required=False)
#     attachment = forms.FileField(label='Attachment', required=False)
    

