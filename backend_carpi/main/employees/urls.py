# employees/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet

urlpatterns = [
    path('employees/', EmpleadoViewSet)
]

router = DefaultRouter()
urlpatterns += router.urls