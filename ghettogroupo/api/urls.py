from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.urls import path, include

from api.views import EditTasksViewSet, CreateTasksViewSet, CreateQuizViewSet, UpdateQuizViewSet

router = DefaultRouter()
router.register('edit-tasks', EditTasksViewSet, basename='edit-tasks-api')
router.register('create-tasks', CreateTasksViewSet, basename='create-tasks-api')
router.register('create-quiz', CreateQuizViewSet)
router.register('update-quiz', UpdateQuizViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Ghettogroupo API Docs",
        default_version='v1',
        description="Test Description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='swagger')
]
