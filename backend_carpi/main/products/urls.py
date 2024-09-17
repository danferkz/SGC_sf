# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PuertaViewSet, VentanaViewSet, MuebleViewSet, ProductoPedidoViewSet

router = DefaultRouter()
router.register(r'puertas', PuertaViewSet)
router.register(r'ventanas', VentanaViewSet)
router.register(r'muebles', MuebleViewSet)
router.register(r'productos_pedido', ProductoPedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
