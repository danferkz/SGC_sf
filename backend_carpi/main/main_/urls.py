
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
schema_view = get_schema_view(
    openapi.Info(
        title="Endpoitns API Carpinteria",
        default_version='v1',
        description="API documentacion para la gestion de una carpinteria",
        terms_of_service="https://www.madereraelbosque.com/policies/terms/",
        contact=openapi.Contact(email="daniel.garciac@usil.pe"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Administración de Django
    path('admin/', admin.site.urls),

    # Rutas para la aplicación de usuarios (clients y admins)
    path('api/users/', include('users.urls')),
    path('api/employees/', include('employees.urls')),  # Incluye las URLs de la aplicación employees
    path('api/products/', include('products.urls')),  # Incluye las URLs de la aplicación products
    path('api/deliveries/', include('deliveries.urls')),  # Incluye las URLs de la aplicación deliveries

    # Swagger URLs
    #re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Aquí puedes incluir otras rutas de otras aplicaciones
    # path('api/other-app/', include('other_app.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
