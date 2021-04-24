from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from user.views import UserCustomViewSet, UserCreateViewSet
from main.views import TodoModelViewSet, ProjectModelViewSet, TodoUsuallyModelViewSet
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
   openapi.Info(
      title="My app todo",
      default_version='0.1',
      description="Documentation to out project",
      contact=openapi.Contact(email="admin@admin.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)
router.register('todo-usually', TodoUsuallyModelViewSet)
# router.register('users', UserCustomViewSet)
router.register('users-create', UserCreateViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/users/0.1', include('user.urls', namespace='0.1')),
    path('api/users/0.2', include('user.urls', namespace='0.2')),
    path('api-token-auth/', views.obtain_auth_token),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),

]
