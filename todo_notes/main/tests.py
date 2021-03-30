import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectModelViewSet
from .models import Project, Todo
from rest_framework.authtoken.models import Token


class TestProjectViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', {'name': 'my test project',
                                                  'users': ['7fe1746d-576d-44ba-a87a-5347816465f1']}, format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail(self):
        project = Project.objects.create(uuid="c390812d-d14c-42de-9754-30fb69875081",
                                         name="тестовый проект",
                                         repository="")
        client = APIClient()
        response = client.get(f'/api/projects/{project.uuid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTodoViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_create(self):
        user = {'username': 'Vasya', 'firstname': 'Ivanov', 'lastname':'Ivan', 'email': 'ivanow@mail.ru'}
        response = self.client.post('/api/users-create/', user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_project(self):
        project = mixer.blend(Project)
        test_name = project.name
        get_project = Project.objects.get(uuid=project.uuid)
        self.assertEqual(get_project.name, test_name)
