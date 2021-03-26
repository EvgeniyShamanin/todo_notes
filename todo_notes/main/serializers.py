from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, StringRelatedField
from .models import Project, Todo
from user.serializers import UserModelSerializer, UserHyperlinkedModelSerializer


class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class TodoModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()
    class Meta:
        model = Todo
        fields = "__all__"

