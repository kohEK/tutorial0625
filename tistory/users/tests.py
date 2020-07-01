from django.contrib.auth import get_user_model
from model_bakery import baker

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make(User, _quantity=3)

        # self.token = Token.objects.create(user=self.users[0])

    def test_should_list(self):
        print('test_get')
        user = self.users[0]
        response = self.client.get('/api/users/')
        print(response)
        self.client.force_authenticate(user=user)
        # print("!!!!!!!!!user!!!!!!!!!!!", self.users)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_should_register(self):
        print('test_register')
        # data -> 회원가입을 할 데이터
        data = {
            # 회원 가입을 시킬 username
            'username': 'username',
            # 회원 가입을 시킬 password
            'password': 'password'
        }
        response = self.client.post('/api/users/register/', data=data)
        print("!!!!!!!!!response.data!!!!!!!!!!!", response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['username'], data['username'])

    def test_should_login(self):
        print('test_login')
        user = baker.make('users.User')
        password = 'password'
        user.set_password(password)
        user.save()
        data = {
            # 회원 가입을 시킬 username
            'username': user.username,
            # 회원 가입을 시킬 password
            'password': 'password'
        }

        response = self.client.post('/api/users/login/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['token'])

    def test_should_logout(self):
        print('test_logout')

        token = Token.objects.create(user=self.users[0])
        self.client.force_authenticate(user=self.users[0])

        response = self.client.delete('/api/users/logout/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertFalse(response.data)
        # self.fail()

    def test_should_update(self):
        print('test_user_update')
        self.client.force_authenticate(user=self.users[0])

        prev_email = self.users[0].email
        data = {
            'email': 'username@naver.com',

        }
        response = self.client.patch(f'/api/users/{self.users[0].id}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['email'], prev_email)
        self.fail()
