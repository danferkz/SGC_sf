
# employees/urls.py
from django.urls import path
from .views import (
    EmployeeCreateView,
    EmployeeListView,
    EmployeeUpdateView,
    # Puedes agregar aquí más vistas relacionadas con empleados en el futuro
)

urlpatterns = [
    # ============ VISTAS DE EMPLEADOS ============ 
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),  # Crear empleado
    # Puedes agregar más rutas para listar, actualizar y eliminar empleados aquí
    path('list/', EmployeeListView.as_view(), name='employee-list'),  # Listar empleados
    path('update/<uuid:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),  # Actualizar empleado
]