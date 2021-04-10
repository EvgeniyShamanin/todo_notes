from django.urls import path
from .views import UserCustomViewSet


app_name = 'user'
urlpatterns = [
    path('', UserCustomViewSet.as_view({'get': 'list'})),
]
