from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.index, name='list'),
    path('todo/<str:pk>/update_todo',views.updateTodo, name='update_todo'),
    path('todo/<str:pk>/delete_todo',views.deleteTodo, name='delete_todo'),
]