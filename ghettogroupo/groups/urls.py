from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from groups.views import group_page_view, groupCreationView, join_group_view
# , add_member

urlpatterns = [
    # url(r'^user/(?P<username>\w+)/(?P<code>[0-9A-Fa-f-]+)$', group_page_view, name='user-group-page'),
    url(r'^user/(?P<code>[0-9A-Fa-f-]+)$', group_page_view, name='group-page'),
    url('create-group', groupCreationView, name='create-group'),
    url('join-group', join_group_view, name='join-group'),
]