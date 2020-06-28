from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, request, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        # serializer = self.serializer_class(data=request.data,
        #                                    context={'request': request})
        # serializer.is_valid(raise_exception=True)
        # username = serializer.validated_data['username']
        # password = serializer.validated_data['password']
        # serializer.save()
        user = authenticate(request=request,
                            username=request.data.get('username'),
                            password=request.data.get('password')
                            )

        if user is None:
            raise NotAuthenticated
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,

        })
        # username = self.request.data.get('username')
        # password = self.request.data.get('password')
        # user = User.objects.get(username=username)
        # if user.check_password(password):
        #     token, __ = Token.objects.get_or_create(user=user)
        #     data = {
        #         "token": token
        #     }
        #     return Response(data, status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def logout(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."},
                        status=status.HTTP_200_OK)
