# users/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientRegistrationView, AdminUserViewSet

urlpatterns = [
    path('register/', ClientRegistrationView.as_view(), name='client-register'),
]

router = DefaultRouter()
router.register(r'admins', AdminUserViewSet)

urlpatterns += router.urls
