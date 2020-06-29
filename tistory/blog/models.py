from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Blog(models.Model):
    # FK 참조시는 str 방식 사용
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#foreignkey
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.related_name
    # related_name은 의미 있는 이름 사용
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=30)
    # TextField는 max_length 제공 안함
    text_post = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    # 명확한 이름 선택
    name = models.CharField(max_length=10, blank=True, default='')
    password = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return self.title


class Comment(models.Model):
    # Class 참조 -> str 참조
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='text_post_set', null=True, blank=True)
    # related_name='comments'
    text_post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='text_post_set')
    text_comment = models.CharField(max_length=255)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.text_comment
