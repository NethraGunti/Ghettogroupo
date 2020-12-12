from django.test import SimpleTestCase
from rest_framework.test import APITestCase
from django.urls import reverse, resolve



class TestUrls(SimpleTestCase):

    def test_detail_url_is_resolved(self):
        assert 1 = 2