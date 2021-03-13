from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer, UserHyperlinkedModelSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import mixins


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserHyperlinkedModelSerializer


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(status=status.HTTP_200_OK)



class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer




