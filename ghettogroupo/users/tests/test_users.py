from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse, resolve


from users.models import User, Interest, UserProfile


class UserTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username='testcaseuser',
            email='testcaseuser@djangotest.com',
            fullName='Test Case User',
            password='testpassword'
        )
        self.user1.save()
        self.interest1 = Interest.objects.create(interest='int1')
        self.interest2 = Interest.objects.create(interest='int2')
    
    def test_user_creation(self):
        self.assertEqual(self.user1.username, 'testcaseuser')
        self.assertTrue(self.user1.email == 'testcaseuser@djangotest.com')
        self.assertEqual(self.user1.fullName, 'Test Case User')
    
    def test_interest_creation(self):
        self.assertEqual(self.interest1.interest, 'int1')
        self.assertEqual(self.interest2.interest, 'int2')