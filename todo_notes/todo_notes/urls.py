from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet, UserModelViewSet, UserCustomViewSet
from main.views import TodoListAPIView, TodoCreateAPIView, TodoModelViewSet, \
    ProjectModelViewSet, TodoRetrieveAPIView, TodoUpdateAPIView, TodoDestroyAPIView

router = DefaultRouter()
router.register('base', UserViewSet, basename='users')
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)
router.register('custom', UserCustomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('viewsets/', include(router.urls)),
    path('custom/', include(router.urls)),
    path('generic/todo/create/', TodoCreateAPIView.as_view()),
    path('generic/todo/list/', TodoListAPIView.as_view()),
    path('generic/todo/retrieve/<int:pk>/', TodoRetrieveAPIView.as_view()),
    path('generic/todo/update/<int:pk>/', TodoUpdateAPIView.as_view()),
    path('generic/todo/destroy/<int:pk>/', TodoDestroyAPIView.as_view()),
]
