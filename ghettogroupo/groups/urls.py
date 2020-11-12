from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from groups.views import test_view

urlpatterns = [
    url(r'^user/(?P<username>\w+)/(?P<code>[0-9A-Fa-f-]+)$', test_view, name='test'),
]