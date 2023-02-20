import email
from django.test import TestCase
from .models import Todo
from django.contrib.auth.models import User

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='12345', email='test@gmail.com')
        Todo.objects.create(title='first todo', memo='memo', important=True, user=user)

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')
    
    def test_memo_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.memo}'
        self.assertEquals(expected_object_name, 'memo')
    
    def test_important_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.important}'
        self.assertEquals(expected_object_name, 'True')

    def test_datecompleted_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.datecompleted}'
        self.assertEquals(expected_object_name, 'None')

    def test_user_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.user}'
        self.assertEquals(expected_object_name, 'testuser')
    
    # def test_created_content(self):
    #     todo = Todo.objects.get(id=1)
    #     expected_object_name = f'{todo.created}'
    #     self.assertEquals(expected_object_name, 'None')
        # self.assertEquals(expected_object_name, '2022-10-14 11:23:41.067000+00:00')

    def test_str_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.__str__()}'
        self.assertEquals(expected_object_name, 'first todo')

