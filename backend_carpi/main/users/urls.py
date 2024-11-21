# users/urls.py
from django.urls import path
from .views import (
    ClientCreateView,
    ClientListView,
    ClientUpdateView,
    ClientProfileView,
    ClientDestroyView,
    ClientDetailView,
    ClientSelfDestroyView,
    AdminCreateView,
    AdminListView,
    AdminUpdateView,
    AdminProfileView,
    AdminDestroyView,
    StaffCreateView,
    StaffListView,
    StaffDestroyView,
    ClientLoginView,
    AdminLoginView,
    LogoutView,
    UserListView,
    ChangePasswordView,
)

urlpatterns = [
    # ============ VISTAS DE CLIENTE ============
    path('clients/', ClientListView.as_view(), name='client-list'),  # Listar clientes
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),  # Crear cliente
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),  # Detalles de cliente
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),  # Actualizar cliente
    path('clients/delete/<int:pk>/', ClientDestroyView.as_view(), name='client-delete'),  # Eliminar cliente
    path('clients/profile/', ClientProfileView.as_view(), name='client-profile'),  # Obtener perfil del cliente
    path('clients/self-delete/', ClientSelfDestroyView.as_view(), name='client-self-delete'),  # Eliminar cuenta del propio cliente

    # ============ VISTAS DE ADMINISTRADOR ============
    path('admins/', AdminListView.as_view(), name='admin-list'),  # Listar administradores
    path('admins/create/', AdminCreateView.as_view(), name='admin-create'),  # Crear administrador
    path('admins/update/<int:pk>/', AdminUpdateView.as_view(), name='admin-update'),  # Actualizar administrador
    path('admins/delete/<int:pk>/', AdminDestroyView.as_view(), name='admin-delete'),  # Eliminar administrador
    path('admins/profile/', AdminProfileView.as_view(), name='admin-profile'),  # Obtener perfil del administrador

    # ============ VISTAS DE STAFF ============
    path('staff/', StaffListView.as_view(), name='staff-list'),  # Listar miembros del staff
    path('staff/create/', StaffCreateView.as_view(), name='staff-create'),  # Crear miembro del staff
    path('staff/delete/<int:pk>/', StaffDestroyView.as_view(), name='staff-delete'),  # Eliminar miembro del staff

    # ============ VISTAS DE AUTENTICACIÓN ============
    path('login/client/', ClientLoginView.as_view(), name='client-login'),  # Login cliente
    path('login/admin/', AdminLoginView.as_view(), name='admin-login'),  # Login administrador
    path('logout/', LogoutView.as_view(), name='logout'),  # Cierre de sesión

    # ============ VISTAS GENERALES ============
    path('users/me/', UserListView.as_view(), name='user-detail'),  # Obtener usuario autenticado
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),  # Cambiar contraseña
]

"""
/clients/?page=1&page_size=10  # Primera página de clientes con 10 elementos
/admins/?page=2&page_size=5    # Segunda página de administradores con 5 elementos
/staff/?page=3                 # Tercera página de personal con el tamaño de página predeterminado

"""
