from django.urls import path
from . import views 

urlpatterns = [
    path('quiz', views.LeaderboardView.as_view(), name="leaderboard"),
]