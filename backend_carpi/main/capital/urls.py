# capital/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CapitalViewSet

router = DefaultRouter()
router.register(r'capital', CapitalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
