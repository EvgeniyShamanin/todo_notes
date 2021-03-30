from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserCustomViewSet, UserCreateViewSet
from main.views import TodoModelViewSet, ProjectModelViewSet, TodoUsuallyModelViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)
router.register('todo-usually', TodoUsuallyModelViewSet)
router.register('users', UserCustomViewSet)
router.register('users-create', UserCreateViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),

]
