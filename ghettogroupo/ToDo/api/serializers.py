from rest_framework import serializers
from ToDo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Todo
        fields = ['id','title','complete']