"""
# employees/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
"""
# employees/urls.py
from django.urls import path
from .views import (
    EmployeeCreateView,
    # Puedes agregar aquí más vistas relacionadas con empleados en el futuro
)

urlpatterns = [
    # ============ VISTAS DE EMPLEADOS ============ 
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),  # Crear empleado
    # Puedes agregar más rutas para listar, actualizar y eliminar empleados aquí
]