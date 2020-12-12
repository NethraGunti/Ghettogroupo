from django.test import TestCase

from users.models import User, UserProfile, Interest


def UserProfileTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username='testcaseuser',
            email='testcaseuser@djangotest.com',
            fullName='Test Case User',
            password='testpassword'
        )
        self.interest1 = Interest.object.create(interest='int1')
        self.interest2 = Interest.object.create(interest='int2')
        self.user1.save()
    
    def test_user_creation(self):
        self.assertEqual(self.user1.username, 'testcaseuser')
        self.assertTrue(self.user1.email == 'testcaseuser@djangotest.com')
        self.assertEqual(self.fullName, 'Test Case User')
    
    # def user_profile_creation(self):
        # self