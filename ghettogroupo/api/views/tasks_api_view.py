from rest_framework import viewsets, permissions
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response

from groups.models import Group, Membership
from tasks.models import Task
from api.permissions import HasTaskCreatePermissions, LimitObejectLevelView
from api.seralizers import EditTaskSerializer, CreateTaskSerializer



class EditTasksViewSet(viewsets.ModelViewSet):
    """
    list:
        allowed users can update/delete existing tasks they have created
    retrieve:
        details of a task
    update:
        edit a task
    delete:
        delete a task
    """
    permission_classes = [permissions.IsAuthenticated, HasTaskCreatePermissions]
    serializer_class = EditTaskSerializer
    http_method_names = ['get', 'put', 'delete']

    def get_queryset(self):
        return Task.objects.filter(assigned_by=self.request.user)
    
    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(assigned_by=user)



class CreateTasksViewSet(viewsets.ModelViewSet):
    """
    list:
        list of all groups a user can assign tasks to
    create:
        allowed users can create new tasks
    retrieve:
        method not allowed
    """
    permission_classes = [permissions.IsAuthenticated, HasTaskCreatePermissions, LimitObejectLevelView]
    serializer_class = CreateTaskSerializer
    http_method_names = ['get', 'post']

    def getUserGroups(self):
        groups_codes = Membership.objects.filter(
            member=self.request.user,
            isAssigner=True).values_list('group', flat=True) or Membership.objects.filter(
                member=self.request.user,
                isOwner=True
            ).values_list('group', flat=True)
        return Group.objects.filter(code__in=groups_codes)

    def get_serializer_context(self):
        return {'groups': self.getUserGroups()}

    def get_queryset(self):
        return Task.objects.filter(assigned_by=self.request.user)
    
    def list(self, request, *args, **kwargs):
        groups = self.getUserGroups()
        return Response(groups.values())
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(assigned_by=user)