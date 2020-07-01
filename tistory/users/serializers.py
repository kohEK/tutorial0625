from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.serializers import BlogSerializer

# from users.models import User
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(source='blog_set', many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    # email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'blog'

        ]

    def create(self, validated_data):
        user = User(username=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user

#
# from django.contrib.auth.models import User
