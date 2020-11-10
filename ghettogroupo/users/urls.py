from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import UserRegisterView, landing_page
urlpatterns = [
    path('register/', UserRegisterView, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('', landing_page, name='landing-page')
    # path('logout/', auth_views.LogoutView.as_view(), name='logout')
]