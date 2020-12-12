from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse, resolve


from groups.models import Group, Membership
from users.models import User
from tasks.models import Task, Subgroup

class GroupTestCase(TestCase):
    def setUp(self):
        self.owner = User.objects.create(
            username='owner',
            email='owner@djangotest.com',
            fullName='Test Case Owner',
            password='testpassword'
        )
        self.owner.save()
        self.assigner = User.objects.create(
            username='assigner',
            email='assigner@djangotest.com',
            fullName='Test Case assigner',
            password='testpassword'
        )
        self.assigner.save()
        self.user1 = User.objects.create(
            username='testcaseuser1',
            email='testcaseuser1@djangotest.com',
            fullName='Test Case User 1',
            password='testpassword'
        )
        self.user1.save()
        self.user2 = User.objects.create(
            username='testcaseuser2',
            email='testcaseuser2@djangotest.com',
            fullName='Test Case User 2',
            password='testpassword'
        )
        self.user2.save()
        self.group = Group.objects.create(
            type='PUBLIC',
            owner=self.owner,
            name='Test Group 1',
            description='test desc 1256e44'
        )
        self.group.save()
        self.assigner_membership = Membership.objects.create(
            group=self.group,
            member=self.assigner,
            isAssigner=True
        )
        self.assigner_membership.save()
        self.user_membership1 = Membership.objects.create(
            group=self.group,
            member=self.user1
        )
        self.user_membership1.save()
        self.user_membership2 = Membership.objects.create(
            group=self.group,
            member=self.user2
        )
        self.user_membership2.save()
        self.task = Task.objects.create(
            assigned_by=self.assigner,
            assigned_group=self.group,
            task_title='Test Task Title',
            task_desc='Test Task Desc'
        )
        self.task.save()

    def test_task_details(self):
        self.assertEqual(self.task.ofGroup(), self.group)    
        self.assertEqual(self.task.ofGroup(), self.group)    