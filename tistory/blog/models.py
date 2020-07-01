from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
# from users.models import User
User = get_user_model()


class Blog(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='blog_set', null=True)
    title = models.CharField(max_length=30)
    text_post = models.TextField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='text_post_set', null=True)
    text_post = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='text_post_set')
    text_comment = models.CharField(max_length=255)


    def __str__(self):
        return self.text_comment
