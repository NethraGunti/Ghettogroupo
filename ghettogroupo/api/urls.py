from rest_framework.routers import DefaultRouter

from django.urls import path, include

from api.views import EditTasksViewSet, CreateTasksViewSet

router = DefaultRouter()
router.register('edit-tasks', EditTasksViewSet, basename='edit-tasks-api')
router.register('create-tasks', CreateTasksViewSet, basename='create-tasks-api')

urlpatterns = [
    path('', include(router.urls))
] 