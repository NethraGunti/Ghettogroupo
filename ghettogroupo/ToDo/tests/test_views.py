from django.test import TestCase, Client
from rest_framework.test import APITestCase
from django.urls import reverse
from ToDo.models import Todo
from users.models import User
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('checklist')
        self.update_url = reverse('update_todo', args=['some-id'])
        self.delete_url = reverse('delete_todo', args=['some-id'])
        self.list_data = {
            "title" : "TestTitle",
            "complete" : "True"
        }
        self.update_data = {
            "title" : "UpdatedTestTitle",
            "complete" : "True"
        }
        
    def test_todo_list_view_post_data(self):
        self.client.post(self.list_url, self.list_data, format="json")
        response = self.client.post(self.list_url)
        self.assertEqual(response.status_code, 302)


    def test_todo_update_view_post_data(self):
        self.client.post(self.update_url, self.update_data, format="json")
        response = self.client.post(self.list_url)
        self.assertEqual(response.status_code, 302)

    def test_todo_delete_view_post_data(self):
        response = self.client.post(self.list_url)
        self.assertEqual(response.status_code, 302)
            
class ApiTestViews(APITestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="Manju",
            email= "manju@gmail.com",
             
        )
        self.user.save()
        self.title =  'testtitle'
        self.complete = 'True'
        self.id = '1'
        self.todo = Todo.objects.create(
            user = self.user,
            id = self.id,
            title = self.title,
            complete = self.complete
        )
        self.todo.save()

        self.list_url = reverse('todo-list')
        self.detail_url = reverse('todo-detail', args=[1])
        
        self.list_data = {
            "user" : "user1",
            "id" : "1",
            "title" : "TestTitle",
            "complete" : "True"
        }
        self.detail_data = {
            "user" : "user1",
            
            "title" : "updatedTestTitle",
            "complete" : "True"
        }

    def test_api_list_view_get(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
    
    def test_api_create_view_post_data(self):
        self.client.post(self.list_url, self.list_data, format='json')
        response = self.client.post(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_api_detail_view_get(self):
        response = self.client.post(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_api_update_view_post_data(self):
        self.client.post(self.detail_url, self.detail_data, format='json')
        response = self.client.post(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_api_delete_view_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)



