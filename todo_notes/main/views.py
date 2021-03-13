from rest_framework import request, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from django_filters import rest_framework as filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, \
    RetrieveUpdateAPIView
import logging

info_log = logging.getLogger('info_logger')


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Todo
        fields = ['project']


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        info_log.info(f'sometest {headers}')
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter
    info_log.info(f'sometest todo {request}')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # kwargs['status'] = False
        update_value = {"text": instance.text, "status": False}
        serializer = self.get_serializer(instance, data=update_value, partial=partial)
        serializer.is_valid(raise_exception=True)
        info_log.info(f'sometest {serializer.data}')
        # return self.update(request, *args, **kwargs)
        return Response(serializer.data)
        #
        # self.perform_destroy(instance)
        # return Response(status=status.HTTP_204_NO_CONTENT)


class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class TodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class TodoRetrieveAPIView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class TodoUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class TodoDestroyAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

    def get(self, request, *args, **kwargs):
        info_log.info(f'test -{request}')
        return self.retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        kwargs['status'] = False
        return self.update(request, *args, **kwargs)
