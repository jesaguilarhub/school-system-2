from rest_framework.test import APITestCase
from courses.models import Course
from django.contrib.auth.models import User

class EditorialTestCase(APITestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.user = User.objects.create_user( 
            username='user',
            email='user@gmail.com',
            password='password'
        )
        
        response = self.client.post(f'{self.host}/api/token/', {'username': 'user', 'password': 'password'} )
        self.token = response.data['access']

    def test_get_user(self):
        response = self.client.get(f'{self.host}/users/1')
        self.user.pop('token')
        self.assertEqual(response.data, self.user)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(
              f'{self.host}/users/',
              data={"username": "algo", "email": "algo@gmail.com", "password": "algo"},
              HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )
        user = User.objects.filter(username='algo')
        self.assertTrue(user.exists())
        self.assertEqual(response.status_code, 201)

    def test_delete_user(self):
        response = self.client.delete(f'{self.host}/users/1')
        user = User.objects.filter(username='user')
        self.assertFalse(user.exists())
        self.assertEqual(response.status_code, 204)
