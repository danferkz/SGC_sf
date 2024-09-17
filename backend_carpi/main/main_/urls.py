
'''
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Backoffice (admin) URLs
    path('backoffice/capital/', include('capital.urls')),
    path('backoffice/deliveries/', include('deliveries.urls')),
    path('backoffice/employees/', include('employees.urls')),
    path('backoffice/orders/', include('orders.urls')),
    path('backoffice/products/', include('products.urls')),
    path('backoffice/users/', include('users.urls')),

    # Frontoffice (customer) URLs
    path('frontoffice/products/', include('products.urls')),  # Los clientes también pueden ver productos
    path('frontoffice/orders/', include('orders.urls')),  # Para que los clientes gestionen sus pedidos
    path('frontoffice/users/', include('users.urls')),  # Registro y gestión de cuentas de usuarios
'''
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views
from django.conf import settings  # Asegúrate de importar settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración de Django

    # Rutas para el JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar token JWT

    path('api/employees/', include('employees.urls')),

    # Incluir las rutas de usuarios
    path('users/', include('users.urls')),  # Incluir URLs definidas en users/urls.py
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)