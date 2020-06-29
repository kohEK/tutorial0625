from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers

from blog.serializers import BlogSerializer


class UserSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(source='blog_set', many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    # email = serializers.EmailField(allow_null=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'id',
            # 'email',
            'blog'

        ]

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user


