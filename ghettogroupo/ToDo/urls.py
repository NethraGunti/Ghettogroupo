from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.index, name='list'),
    path('todo/update_todo/<str:pk>/',views.updateTodo, name='update_todo'),
    path('todo/delete_todo/<str:pk>',views.deleteTodo, name='delete_todo'),
]