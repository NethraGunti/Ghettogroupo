from django.urls import path, include

from developer.views import get_keys, gen_keys

urlpatterns = [
    path('developer/', get_keys, name='developer'),
    path('generate-keys/', gen_keys, name='gen-keys'),
]