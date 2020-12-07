from django.urls import path
from . import views 

urlpatterns = [

    path('todo-list/',views.TodoListView.as_view(), name="todo-list"),
    path('todo-detail/<str:pk>/',views.TodoDetailView.as_view(), name="todo-detail"),
    
]