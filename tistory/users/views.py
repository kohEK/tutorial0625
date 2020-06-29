# Create your views here.

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # create() 기본적으로 처리하는 내용과 동일하므로 필요 없음
    @action(detail=False, methods=['post'])
    def register(self, request):
        # /api/users/register로 요청 받고 싶으면
        # return super().create(request)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        user = authenticate(request=request,
                            username=request.data.get('username'),
                            password=request.data.get('password')
                            )

        if user is None:
            raise NotAuthenticated
        # get_or_create() 호출시 exception 발생 가능
        # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get-or-create
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,

        })

    @action(detail=False, methods=['delete'])
    def logout(self, request):
        request.user.auth_token.delete()
        # status code 다양화
        # https://www.restapitutorial.com/httpstatuscodes.html
        return Response({"detail": "Successfully logged out."},
                        status=status.HTTP_200_OK)
