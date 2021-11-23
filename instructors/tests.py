from rest_framework.test import APITestCase
from instructors.models import Instructor
from django.contrib.auth.models import User

class InstructorTestCase(APITestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.user = User.objects.create_user( 
            username='user',
            email='user@gmail.com',
            password='password'
        )
        
        response = self.client.post(f'{self.host}/api/token/', {'username': 'user', 'password': 'password'} )
        self.token = response.data['access']

        Instructor.objects.create(nombre='test1')
        Instructor.objects.create(nombre='test2')

    def test_get_list(self):
        response = self.client.get(f'{self.host}/courses/', HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data['results']), 0)

    def test_get_instructor(self):
        response = self.client.get(f'{self.host}/instructors/1')
        self.assertEqual(response.data.name, 'test1')
        self.assertEqual(response.status_code, 200)

    def test_create_instructor(self):
        response = self.client.post(
              f'{self.host}/courses/',
              data={"nombre": "algo"},
              HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )
        instructor = Instructor.objects.filter(nombre='algo')
        self.assertTrue(instructor.exists())
        self.assertEqual(response.status_code, 201)
        
    def test_edit_instructor(self):
        edited = {'nombre': 'Nuevo Test'}
        response = self.client.patch(f'{self.host}/instructors/1', edited)
        instructor = Instructor.objects.filter(nombre='Nuevo Test')
        self.assertTrue(instructor.exists())
        self.assertEqual(response.data, instructor)
        self.assertEqual(response.status_code, 200)

    def test_delete_instructor(self):
        response = self.client.delete(f'{self.host}/instructors/2')
        instructor = Instructor.objects.filter(nombre='test2')
        self.assertFalse(instructor.exists())
        self.assertEqual(response.status_code, 204)
