from rest_framework import serializers

from blog.models import Comment, Blog


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # password 같은 credential 노출 될수 있으므로 신중
        fields = ['id', 'owner', 'text_post', 'text_comment', 'username', 'password']


class BlogSerializer(serializers.ModelSerializer):
    text_comment = CommentSerializer(source='text_post_set', many=True, read_only=True)
    owner = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = ['id', 'owner', 'name', 'password', 'title', 'text_post', 'register_date', 'image', 'text_comment']
