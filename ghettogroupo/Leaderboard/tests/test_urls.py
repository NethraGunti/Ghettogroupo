from django.test import SimpleTestCase
from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from Leaderboard.views import LeaderboardView



class TestUrls(SimpleTestCase):

    def test_detail_url_is_resolved(self):
        url = reverse('leaderboard')
        self.assertEquals(resolve(url).func.view_class, LeaderboardView)