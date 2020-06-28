from django.urls import path
from rest_framework import routers

from blog import views
from blog.views import BlogViewSet

router = routers.SimpleRouter(
    # trailing_slash=False
)
router.register(r'blog', BlogViewSet)
# router.register(r'comment', CommentViewSet)

urlpatterns = router.urls

# urlpatterns +=[
#     path('',views.comment_list),
#     path('<int:pk>/',views.comment_detail),
#     ]