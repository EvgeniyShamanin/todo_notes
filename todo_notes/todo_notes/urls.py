from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet, UserModelViewSet, UserCustomViewSet
from main.views import TodoModelViewSet, ProjectModelViewSet

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
]
