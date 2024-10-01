from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import ClientSerializer, AdminSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import PermissionDenied

# 1. Crear un nuevo cliente
class ClientCreateView(CreateAPIView):
    serializer_class = ClientSerializer
    authentication_classes = []
    permission_classes = []

    def perform_create(self, serializer):
        # marcado como cliente
        serializer.save(is_cliente=True)

# 2. Crear un nuevo administrador (solo los administradores pueden crear otros administradores)
class AdminCreateView(CreateAPIView):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save(is_staff=True, is_superuser=True)
        else:
            raise PermissionDenied('Solo los administradores pueden crear otros administradores.')

# 3. Mostrar la lista de clientes (solo los administradores pueden listar a los clientes)
class ClientListView(ListAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return CustomUser.objects.filter(is_cliente=True)
        else:
            raise PermissionDenied('Solo los administradores pueden listar los clientes.')

class AdminListView(ListAPIView):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return CustomUser.objects.filter(is_staff=True)
        else:
            raise PermissionDenied('Solo los administradores pueden listar otros administradores.')

# 5. Actualizar un cliente existente
class ClientUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.filter(is_cliente=True)
    serializer_class = ClientSerializer
    authentication_classes = [JWTAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance:
            return Response({'error': 'Solo puedes actualizar tu propio perfil.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

# 6. Actualizar un administrador existente (solo administradores)
class AdminUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_staff and request.user != instance:
            return Response({'error': 'Solo los administradores pueden actualizar su propio perfil o el de otros administradores.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

# 7. Eliminar un cliente existente (eliminación lógica usando "is_active" a false)
class ClientDestroyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            cliente = CustomUser.objects.get(pk=pk, is_cliente=True)
            cliente.is_active = False
            cliente.save()
            return Response({'message': 'Cliente eliminado lógicamente.'}, status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Cliente no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
# 8. Eliminar un administrador existente (eliminación física usando DestroyAPIView)
class AdminDestroyView(DestroyAPIView):
    queryset = CustomUser.objects.filter(is_staff=True)
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

# 9. Login para Clientes
class ClientLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if not user.is_cliente:
            raise serializers.ValidationError("Solo los clientes pueden acceder.")
        return data

class ClientLoginView(TokenObtainPairView):
    serializer_class = ClientLoginSerializer

# 10. Login para Administradores
class AdminLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if not user.is_staff:
            raise serializers.ValidationError("Solo los administradores pueden acceder.")
        return data

class AdminLoginView(TokenObtainPairView):
    serializer_class = AdminLoginSerializer

# 11. Logout para Administradores y Clientes
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout exitoso."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
