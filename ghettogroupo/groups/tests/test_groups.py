from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse, resolve


from groups.models import Group, Membership
from users.models import User


class GroupTestCase(TestCase):
    def setUp(self):
        self.owner = User.objects.create(
            username='owner',
            email='owner@djangotest.com',
            fullName='Test Case Owner',
            password='testpassword'
        )
        self.owner.save()
        self.manager = User.objects.create(
            username='manager',
            email='manager@djangotest.com   ',
            fullName='Test Case Manager',
            password='testpassword'
        )
        self.manager.save()
        self.assigner = User.objects.create(
            username='assigner',
            email='assigner@djangotest.com',
            fullName='Test Case assigner',
            password='testpassword'
        )
        self.assigner.save()
        self.user = User.objects.create(
            username='testcaseuser',
            email='testcaseuser@djangotest.com',
            fullName='Test Case User',
            password='testpassword'
        )
        self.user.save()
        self.group = Group.objects.create(
            type='PUBLIC',
            owner=self.owner,
            name='Test Group 1',
            description='test desc 1256e44'
        )
        self.group.save()
        self.owner_membership = Membership.objects.create(
            group=self.group,
            member=self.owner,
            isOwner=True,
        ).save()
        self.manager_membership = Membership.objects.create(
            group=self.group,
            member=self.manager,
            isManager=True,
        ).save()
        self.assigner_membership = Membership.objects.create(
            group=self.group,
            member=self.assigner,
            isAssigner=True
        ).save()
        self.user_membership = Membership.objects.create(
            group=self.group,
            member=self.user
        ).save()

    def test_owner_perm(self):
        self.assertTrue(self.owner.hasOwnerPerm())
        self.assertTrue(self.owner.hasAssignerPerm())
        self.assertTrue(self.owner.hasManagerPerm())
    
    def test_manager_perm(self):
        self.assertFalse(self.manager.hasOwnerPerm())
        self.assertFalse(self.manager.hasAssignerPerm())
        self.assertTrue(self.manager.hasManagerPerm())

    def test_assigner_perm(self):
        self.assertFalse(self.assigner.hasOwnerPerm())
        self.assertTrue(self.assigner.hasAssignerPerm())
        self.assertFalse(self.assigner.hasManagerPerm())
    