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

        Course.objects.create(nombre='test1')
        Course.objects.create(nombre='test2')

    def test_get_list(self):
        response = self.client.get(f'{self.host}/courses/', HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data['results']), 0)

    def test_get_course(self):
        response = self.client.get(f'{self.host}/courses/1')
        self.assertEqual(response.data.name, 'test1')
        self.assertEqual(response.status_code, 200)

    def test_create_course(self):
        response = self.client.post(
              f'{self.host}/courses/',
              data={"nombre": "algo"},
              HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )
        course = Course.objects.filter(nombre='algo')
        self.assertTrue(course.exists())
        self.assertEqual(response.status_code, 201)
        
    def test_edit_course(self):
        edited = {'nombre': 'Nuevo Test'}
        response = self.client.patch(f'{self.host}/courses/1', edited)
        course = Course.objects.filter(nombre='Nuevo Test')
        self.assertTrue(course.exists())
        self.assertEqual(response.data, course)
        self.assertEqual(response.status_code, 200)

    def test_delete_course(self):
        response = self.client.delete(f'{self.host}/courses/2')
        course = Course.objects.filter(nombre='test2')
        self.assertFalse(course.exists())
        self.assertEqual(response.status_code, 204)
