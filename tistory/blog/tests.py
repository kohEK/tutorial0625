from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker

from blog.models import User, Comment, Blog

"""
    ** comment
    1. commnent CRUD -->> setUp 을 써야 되는게 list
    2. 존재하는 포스트가 있을거고, 존재하는 유저가 있을텐데 이걸 쓰레기값으로 확인할 수 있나?
    3. 주입한 포스트와 유저를 사용해서 댓글을 만들고
    4. 이 댓글이 우리가 setup 에서 생성한, post, User가 맞는지??
    setUp   - 포스트랑 유저를 만든다.(post, user)
            - 코멘트를 우선 하나만 (post, user) 만든다.
    list - 셋업에서 만든 comment 가 올바르게 잘 리턴 되었는지 확인.
    create - data 에 담아서 post요청을 보낸다. 
           - response를 잘 받아서 비교한다. 
"""


class CommnetTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make(User, _quantity=3)
        self.blog = Blog.objects.create(owner=self.users[0],
                                        text_post='test_post')
        self.comment = Comment.objects.create(owner=self.users[0],
                                              text_post=self.blog,
                                              text_comment='text_comment'
                                              )

    def test_should_Comment_list(self):
        print('test_Comment_get')
        user = self.users[0]
        response = self.client.get('/api/comment/')
        self.client.force_authenticate(user=user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_Comment_create(self):
        print('test_Comment_create')
        # user = self.user
        # self.client.force_authenticate(user=user)
        data = {
            "text_comment": "test",
            "text_post": "1",
            "owner": "1"
        }
        response = self.client.post('/api/comment/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['text_comment'])
        self.assertTrue(response.data['text_post'])
        self.assertEqual(response.data['text_comment'], data['text_comment'])

    def test_should_Comment_update(self):
        print('test_Comment_update')
        user = self.users[0]
        self.client.force_authenticate(user=user)
        prev_comment = self.comment.text_comment
        data = {
            "owner": 1,
            "text_comment": "changed_comment",
            "text_post": 1,
        }

        response = self.client.patch(f'/api/comment/{self.comment.id}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text_post'], data['text_post'])
        self.assertNotEqual(response.data['text_comment'], prev_comment)

    def test_should_Comment_delete(self):
        print('test_Comment_delete')
        user = self.users[0]
        self.client.force_authenticate(user=user)

        response = self.client.delete(f'/api/comment/{self.comment.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BlogTestCase(APITestCase):

    def setUp(self) -> None:
        self.users = baker.make(User, _quantity=3)
        self.blog = Blog.objects.create(owner=self.users[0],
                                        text_post='test_post')

    def test_should_blog_list(self):
        user = self.users[0]
        response = self.client.get('/api/blog/')
        self.client.force_authenticate(user=user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_blog_create(self):
        print('blog_create')
        user = self.users[0]
        # data = 넘겨줄 blog 내용  ****
        data = {
            "owner": 1,
            "title": "test_title",
            "text_post": "test_post",
        }

        response = self.client.post('/api/blog/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['text_post'], data['text_post'])
        self.assertTrue(user.username)

    def test_should_blog_update(self):
        print('blog_update')
        user = self.users[0]
        self.client.force_authenticate(user=user)
        prev_post = self.blog.text_post

        data = {
            "title": "test_title",
            "text_post": "changed_post"
        }

        response = self.client.patch(f'/api/blog/{self.blog.id}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertNotEqual(response.data['text_post'], prev_post)

    def test_should_blog_delete(self):
        print('blog_delete')
        user = self.users[0]
        self.client.force_authenticate(user=user)

        response = self.client.delete(f'/api/blog/{self.blog.id}/')

        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertFalse(response.data)


        self.fail()
