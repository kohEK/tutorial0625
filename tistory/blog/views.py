from rest_framework.viewsets import ModelViewSet

from blog.models import Blog, Comment
from blog.serializers import BlogSerializer, CommentSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

