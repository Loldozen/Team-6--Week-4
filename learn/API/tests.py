from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model 
from rest_framework.test import APITestCase
from rest_framework import status 

# Create your tests here.
User = get_user_model()
class UserTest(APITestCase):
    
    def setUp(self):
        self.test_user = User.objects.create_user('usertest','test@gmail.com', 'testing123')
        self.create_url = reverse('api-register')

    def test_create_user(self):
        data={
            'username':'example',
            'email':'example@gmail.com',
            'password':'random123',
        }
        response = self.client.post(self.create_url, data, format=None)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data )
    
    def test_create_children_profile(self):
        pass