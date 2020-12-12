from django.test import SimpleTestCase
from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from ToDo.views import index, updateTodo, deleteTodo
from ToDo.api.views import TodoListView, TodoDetailView


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, index)

    def test_add_url_is_resolved(self):
        url = reverse('update_todo', args=['some-id'])
        self.assertEquals(resolve(url).func, updateTodo)

    def test_delete_url_is_resolved(self):
        url = reverse('delete_todo', args=['some-id'])
        self.assertEquals(resolve(url).func, deleteTodo)


class TestAPIUrls(APITestCase):

    def test_list_url_is_resolved(self):
        url = reverse('todo-list')
        self.assertEquals(resolve(url).func.view_class, TodoListView)

    def test_detail_url_is_resolved(self):
        url = reverse('todo-detail', args=['some-id'])
        self.assertEquals(resolve(url).func.view_class, TodoDetailView)