from rest_framework import serializers

from blog.models import Comment, Blog


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['owner', 'text_post','text_comment', 'username', 'password']


class BlogSerializer(serializers.ModelSerializer):
    text_comment = CommentSerializer(source='text_post_set', many=True, read_only=True)
    owner = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = ['owner', 'name', 'password', 'title', 'text_post', 'register_date', 'image', 'text_comment']
