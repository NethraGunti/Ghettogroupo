from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('test/', views.test_print, name='test'),
    url(r'^user/(?P<code>[0-9A-Fa-f-]+)/create-quiz/$',
        views.quiz_creation_view, name='create'),
    url(r'^user/(?P<qid>[0-9A-Fa-f-]+)/add-questions/$',
        views.create_question_set, name='add-questions'),
    url(r'^user/(?P<question>[0-9A-Fa-f-]+)/add-choices/$',
        views.create_question_set, name='add-choices')

]
