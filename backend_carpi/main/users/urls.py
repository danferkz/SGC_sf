from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'admin', views.AdminUserViewSet, basename='admin_users')

urlpatterns = [
    # Registro de clientes
    path('register/', views.ClientRegistrationView.as_view(), name='register_clients'),
    
    # Login de clientes
    path('login/client/', views.ClientLoginView.as_view(), name='login_clients'),
    
    # Login de administradores
    path('login/admin/', views.AdminLoginView.as_view(), name='login_admins'),
    
    # CRUD de usuarios administradores
    path('', include(router.urls)),  # Registra las rutas del viewset
]
