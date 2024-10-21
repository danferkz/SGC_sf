from django.urls import path
from .views import (
    ClientCreateView, AdminCreateView,
    ClientListView, AdminListView,
    ClientUpdateView, AdminUpdateView,
    ClientDestroyView, AdminDestroyView,
    ClientLoginView, AdminLoginView, LogoutView,
    AdminProfileView, ClientProfileView,
    ChangePasswordView
)

urlpatterns = [
    # Creación de usuarios
    path('clients/create/', ClientCreateView.as_view(), name='create-client'),
    path('admins/create/', AdminCreateView.as_view(), name='create-admin'),

    # Listado de usuarios
    path('clients/', ClientListView.as_view(), name='list-clients'),
    path('admins/', AdminListView.as_view(), name='list-admins'),

    # Actualización de usuarios
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='update-client'),
    path('admins/update/<int:pk>/', AdminUpdateView.as_view(), name='update-admin'),

    # Cambio de contraseña
    path('clients/change-password/', ChangePasswordView.as_view(), name='change-password-client'),  # Nueva URL

    # Eliminación de usuarios
    path('clients/delete/<int:pk>/', ClientDestroyView.as_view(), name='delete-client'),
    path('admins/delete/<int:pk>/', AdminDestroyView.as_view(), name='delete-admin'),

    # Autenticación
    path('clients/login/', ClientLoginView.as_view(), name='login-client'),
    path('admins/login/', AdminLoginView.as_view(), name='login-admin'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Perfiles
    path('admins/profile/', AdminProfileView.as_view(), name='admin-profile'),
    path('clients/profile/', ClientProfileView.as_view(), name='client-profile'),
]
