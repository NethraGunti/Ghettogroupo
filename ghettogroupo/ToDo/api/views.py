from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TodoSerializer
from ToDo.models import Todo



class TodoListView(generics.GenericAPIView):
    serializer_class = TodoSerializer
    def get(self,request):
        self.queryset = Todo.objects.all()
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        return Response(serializer.data)


class TodoDetailView(generics.GenericAPIView):
    serializer_class = TodoSerializer
    def get(self,request, pk):
        task = Todo.objects.get(id=pk)
        serializer = self.serializer_class(task, many=False)
        return Response(serializer.data)
    
    def post(self, request, pk):
        task = Todo.objects.get(id=pk)
        serializer = self.serializer_class(instance=task, data = request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete(self, request,pk):
        task = Todo.objects.get(id=pk)
        task.delete()
        return Response('Task Succuessfully deleted!')



