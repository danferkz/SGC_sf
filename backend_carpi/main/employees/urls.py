<<<<<<< HEAD

# employees/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

=======
>>>>>>> aa0943055347aeec60d19ae8d698ba29e7c97134
