from rest_framework import serializers
from users.models import User
from quizzes.models import *


class LeaderboardSerializer(serializers.ModelSerializer):

    class Meta:
        model=Quiz
        fields = ['creator']