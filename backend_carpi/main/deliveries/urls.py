# deliveries/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntregaViewSet

router = DefaultRouter()
router.register(r'entregas', EntregaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
