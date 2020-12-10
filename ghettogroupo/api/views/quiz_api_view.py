from rest_framework import viewsets, permissions, status
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
import json

from quizzes.models import Quiz, Question, Choice
from groups.models import Group, Membership
from api.permissions import HasTaskCreatePermissions, LimitObejectLevelView, HasQuizUpdatePermissions
from api.seralizers import CreateQuizSerializer, UpdateQuizSerializer


class CreateQuizViewSet(viewsets.ModelViewSet):
    serializer_class = CreateQuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [permissions.IsAuthenticated,
                          HasTaskCreatePermissions, LimitObejectLevelView]
    http_method_names = ['get', 'post']

    def getUserGroups(self):
        groups_codes = Membership.objects.filter(
            member=self.request.user,
            isAssigner=True).values_list('group', flat=True) or Membership.objects.filter(
                member=self.request.user,
                isOwner=True
        ).values_list('group', flat=True)
        return Group.objects.filter(code__in=groups_codes)

    def list(self, request, *args, **kwargs):
        groups = self.getUserGroups()
        return Response(groups.values())

    def get_queryset(self):
        return Quiz.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        # print(serializer)
        serializer.save(user=user)
        # questions = serializer.data["questions"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        return Response({'200': 'Quiz object has been created successfully'}, status=status.HTTP_201_CREATED)


class UpdateQuizViewSet(viewsets.ModelViewSet):
    """docstring for UpdateQuizViewSet."""
    serializer_class = UpdateQuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [permissions.IsAuthenticated,
                          HasQuizUpdatePermissions]
    http_method_names = ['get', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        # groups = self.getUserGroups()
        return Response(Quiz.objects.filter(creator=request.user).values())
