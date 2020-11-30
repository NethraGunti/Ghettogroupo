from django.urls import path
from django.conf.urls import url

from tasks.views import create_task

urlpatterns = [
    url(r'user/(?P<code>[0-9A-Fa-f-]+)/create-task/', create_task, name='create-task'),
]