from model_bakery import baker

from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make('auth.User', _quantity=3)
        # Token 불필요
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

        # 실제로 response 주는 필드 확인 필요
        for user_response in response.data:
            self.assertEqual(user_response['username'])
            self.assertEqual(user_response['id'])
            self.assertEqual(user_response['blog'])

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
        user = baker.make('auth.User')
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

        response = self.client.delete('/api/users/logout/', data=data)

        self.fail()
