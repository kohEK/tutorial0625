from rest_framework import serializers

from blog.models import Comment, Blog


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['owner', 'text_post', 'text_comment']


class BlogSerializer(serializers.ModelSerializer):
    text_comment = CommentSerializer(source='text_post_set', many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='User')

    class Meta:
        model = Blog
        fields = ['owner', 'title', 'text_post', 'register_date', 'image', 'text_comment']
        # read_only_fields = ('owner',)
