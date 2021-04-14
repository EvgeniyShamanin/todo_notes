from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import User


class UserHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserModelUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'is_superuser', 'is_staff']
