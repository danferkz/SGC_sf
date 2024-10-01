"""
URL configuration for main_ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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

urlpatterns = [
    # Administración de Django
    path('admin/', admin.site.urls),

    # Rutas para la aplicación de usuarios (clients y admins)
    path('api/users/', include('users.urls')),

    # Aquí puedes incluir otras rutas de otras aplicaciones
    # path('api/other-app/', include('other_app.urls')),
]
