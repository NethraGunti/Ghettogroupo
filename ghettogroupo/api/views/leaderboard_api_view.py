from collections import OrderedDict

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from api.serializers import LeaderboardSerializer

from quizzes.models import *
from users.models import *

class LeaderboardView(generics.GenericAPIView):
    serializer_class = LeaderboardSerializer

    def post(self,request):
        data = request.data
        self.queryset = Quiz.objects.all()
        serializer = self.serializer_class(data)
        data = serializer.data
        quiz_num = data['quiz_num']
        quiz_num = int(quiz_num)-1

        question_list = []
        for i in range(len(self.queryset)):
            question_list.append(Question.objects.filter(quiz=self.queryset[i]))
        
        choice_list = []
        for i in range(len(question_list)):
            for j in range(len(question_list[i])):
                choice_list.append(Choice.objects.filter(question=question_list[i][j]))
        # return Response(data=choice_list)

        response_list = []
        for i in range(len(choice_list)):
            for j in range(len(choice_list[i])):
                response_list.append(Responses.objects.filter(choice=choice_list[i][j]))

        respondants = []
        for i in range(len(response_list)):
            for j in range(len(response_list[i])):
                respondants.append(response_list[i][j].respondant)
        respondants = list(set(respondants))

        marks = []
        # for i in range(len(self.queryset)):
        for i in range(len(respondants)):
            marks.append(User.get_marks(respondants[i],self.queryset[quiz_num])) 
        
        # leaderboard = {}
        leaderboard_list =[]
        for i in range(len(respondants)):
            # leaderboard['respondant'] = respondants[i].username
            leaderboard = {
                'respondant' :  respondants[i].username,
                'total_marks' : marks[i]    
            }
            # leaderboard['total_marks'] = marks[i]
            leaderboard_list.append(leaderboard)

        leaderboard_list = sorted(leaderboard_list,key=lambda ele: ele['total_marks'],reverse=True)
        return Response(leaderboard_list)