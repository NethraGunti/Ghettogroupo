from django.urls import path

from general.views import landing_page, dashboard

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('dashboard', dashboard, name='dashboard'),
]