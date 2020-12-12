from rest_framework import serializers

from tasks.models import Task, Subgroup


#COMMENTED OUT TO ADD IT BACK AFTER SHIFTING TO POSTGRESS

# class SubgroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subgroup
#         fields = '__all__'

class EditTaskSerializer(serializers.ModelSerializer):
    # subgroup = SubgroupSerializer(required=False, help_text='list of usernames part of the subgroup. leave empty for all')
    class Meta:
        model = Task
        exclude = ['assigned_by', 'assigned_group']
        # include = ['subgroup']



class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['assigned_by']
    
    def __init__(self, *args, **kwargs):
        groups = kwargs.pop('context')['groups']
        super(CreateTaskSerializer, self).__init__(*args, **kwargs)
        self.fields['assigned_group'] = serializers.PrimaryKeyRelatedField(queryset=groups)





        
        