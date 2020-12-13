from rest_framework import serializers
from users.models import User
from quizzes.models import *


class LeaderboardSerializer(serializers.Serializer):
    quiz_num = serializers.IntegerField()

    class Meta:
        fields = ['quiz_num']





            

