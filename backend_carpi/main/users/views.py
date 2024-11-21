# users/views.py
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import PermissionDenied
from .models import CustomUser
from .serializers import (
    ClientSerializer, 
    AdminSerializer, 
    ClientProfileUpdateSerializer,
    ChangePasswordSerializer,
    StaffSerializer,
    AdminProfileUpdateSerializer
)

# Permisos personalizados
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)  # Verifica si el usuario es superusuario

# Vistas Base
class BaseAuthenticatedView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

# ============ VISTAS DE CLIENTE ============

# Vista para crear un nuevo cliente
class ClientCreateView(CreateAPIView):
    serializer_class = ClientSerializer
    authentication_classes = []
    permission_classes = []

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_client = True
        user.save()

# Vista para listar todos los clientes
class ClientListView(ListAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return CustomUser.objects.filter(is_client=True)

# Vista para actualizar el perfil de un cliente
class ClientUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.filter(is_client=True)
    serializer_class = ClientProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        obj = super().get_object()
        if obj != self.request.user:
            raise PermissionDenied("Solo puedes actualizar tu propio perfil.")
        if not obj.is_active:
            raise PermissionDenied("Este cliente está inactivo y no puede actualizar su perfil.")
        return obj

# Vista para obtener el perfil del cliente autenticado
class ClientProfileView(BaseAuthenticatedView):
    def get(self, request):
        user = request.user
        if not user.is_client:
            raise PermissionDenied("No eres un cliente")
        if not user.is_active:
            raise PermissionDenied("Este cliente está inactivo")
        serializer = ClientSerializer(user)
        return Response(serializer.data)

# Vista para eliminar un cliente
class ClientDestroyView(BaseAuthenticatedView):
    def delete(self, request, pk):
        try:
            cliente = CustomUser.objects.get(pk=pk, is_client=True)
            if not request.user.is_superuser:  # Cambiado a is_superuser
                raise PermissionDenied("No tienes permisos para realizar esta acción")
            cliente.is_active = False
            cliente.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Cliente no encontrado'}, 
                status=status.HTTP_404_NOT_FOUND
            )

# Vista para obtener los datos de un cliente específico
class ClientDetailView(BaseAuthenticatedView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    authentication_classes = [JWTAuthentication]  # Usa JWT para la autenticación

    def get(self, request, pk):
        try:
            cliente = CustomUser.objects.get(pk=pk, is_client=True)  # Obtiene el cliente por ID
            if cliente != request.user:  # Verifica que el cliente sea el mismo que está haciendo la solicitud
                raise PermissionDenied("No tienes permiso para ver los datos de este cliente.")
            serializer = ClientSerializer(cliente)  # Serializa los datos del cliente
            return Response(serializer.data)  # Retorna los datos del cliente
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Cliente no encontrado'}, 
                status=status.HTTP_404_NOT_FOUND  # Maneja el caso en que el cliente no existe
            )
            

# Vista para que un cliente elimine su propia cuenta
class ClientSelfDestroyView(BaseAuthenticatedView):
    def delete(self, request):
        user = request.user
        # Verifica que el usuario sea un cliente y esté autenticado
        if not user.is_client:
            raise PermissionDenied("No tienes permisos para realizar esta acción")
        if not user.is_active:
            return Response(
                {'error': 'Esta cuenta ya está inactiva'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Realiza la eliminación lógica
        user.is_active = False
        user.save()
        return Response(
            {'message': 'Tu cuenta ha sido eliminada exitosamente.'},
            status=status.HTTP_204_NO_CONTENT
        )

# ============ VISTAS DE ADMINISTRADOR ============

# Vista para crear un nuevo administrador
class AdminCreateView(CreateAPIView):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_superuser = True  # Solo se establece is_superuser
        user.save()

# Vista para listar todos los administradores
class AdminListView(ListAPIView):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return CustomUser.objects.filter(is_superuser=True)

# Vista para actualizar un administrador
class AdminUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.filter(is_superuser=True)
    serializer_class = AdminProfileUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

# Vista para obtener el perfil del administrador autenticado
class AdminProfileView(BaseAuthenticatedView):
    def get(self, request):
        if not request.user.is_superuser:  # Cambiado a is_superuser
            raise PermissionDenied("No eres un administrador")
        serializer = AdminProfileUpdateSerializer(request.user)
        return Response(serializer.data)

# Vista para eliminar un administrador
class AdminDestroyView(DestroyAPIView):
    queryset = CustomUser.objects.filter(is_superuser=True)
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

# ============ VISTAS DE STAFF ============

# Vista para crear un nuevo miembro del staff
class StaffCreateView(CreateAPIView):
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_staff = True  # Aquí se sigue usando is_staff para el staff
        user.save()

# Vista para listar todos los miembros del staff
class StaffListView(ListAPIView):
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return CustomUser.objects.filter(is_staff=True, is_superuser=False)

# Vista para eliminar un miembro del staff
class StaffDestroyView(DestroyAPIView):
    """
    Permite que un administrador elimine un miembro del staff. 
    Solo superusuarios tienen permiso para eliminar.
    """
    queryset = CustomUser.objects.filter(is_staff=True, is_superuser=False)
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, *args, **kwargs):
        """
        Realiza la eliminación física de un miembro del staff y proporciona una respuesta personalizada.
        """
        instance = self.get_object()
        instance.delete()  # Realiza la eliminación definitiva
        return Response({"detail": "Miembro del staff eliminado exitosamente."}, status=status.HTTP_204_NO_CONTENT)

# ============ VISTAS DE AUTENTICACIÓN ============

# Serializador para el inicio de sesión de clientes
class ClientLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if not self.user.is_client:
            raise PermissionDenied("Solo los clientes pueden acceder")
        if not self.user.is_active:
            raise PermissionDenied("Esta cuenta está inactiva")
        return data

# Serializador para el inicio de sesión de administradores
class AdminLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if not self.user.is_superuser:  # Cambiado a is_superuser
            raise PermissionDenied("Solo los administradores pueden acceder")
        return data

# Vista para el inicio de sesión de clientes
class ClientLoginView(TokenObtainPairView):
    serializer_class = ClientLoginSerializer

# Vista para el inicio de sesión de administradores
class AdminLoginView(TokenObtainPairView):
    serializer_class = AdminLoginSerializer

# Vista para el cierre de sesión
class LogoutView(BaseAuthenticatedView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]  # Obtiene el token de refresco del request
            token = RefreshToken(refresh_token)  # Crea un token a partir del token de refresco
            token.blacklist()  # Añade el token a la lista negra
            return Response(status=status.HTTP_205_RESET_CONTENT)  # Responde con éxito
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST  # Maneja errores durante el cierre de sesión
            )

# ============ VISTAS GENERALES ============

# Vista para listar el usuario autenticado
class UserListView(ListAPIView):
    serializer_class = ClientSerializer  # Define el serializer a usar
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    authentication_classes = [JWTAuthentication]  # Usa JWT para la autenticación

    def get_queryset(self):
        # Devuelve solo el usuario autenticado
        return CustomUser.objects.filter(id=self.request.user.id)

# Vista para cambiar la contraseña del usuario
class ChangePasswordView(BaseAuthenticatedView):
    def put(self, request):
        user = request.user
        if not user.is_client and not user.is_superuser:
            raise PermissionDenied("No tienes permisos para realizar esta acción")
        
        serializer = ChangePasswordSerializer(
            data=request.data, 
            context={'request': request}  # Pasa el contexto del request al serializer
        )
        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])  # Cambia la contraseña
            user.save()  # Guarda los cambios
            return Response(status=status.HTTP_200_OK)  # Responde con éxito
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Maneja errores de validación
