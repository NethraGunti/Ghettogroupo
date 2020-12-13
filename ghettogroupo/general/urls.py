from django.urls import path

from general.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing-page')
]