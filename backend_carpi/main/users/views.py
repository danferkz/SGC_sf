from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .serializers import ClientRegistrationSerializer, AdminUserSerializer
from .models import CustomUser

class ClientRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ClientRegistrationSerializer
    permission_classes = [AllowAny]

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_staff=True) | CustomUser.objects.filter(is_superuser=True)
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({'error': 'No tienes permiso para crear otros administradores.'}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    # Los otros métodos CRUD ya están bien implementados y protegidos por IsAdminUser
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ClientLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data
            username = request.data.get('username')
            user = CustomUser.objects.filter(username=username).first()
            if user and not user.is_cliente:
                return Response({'error': 'No tienes permiso para acceder a esta área'}, status=status.HTTP_403_FORBIDDEN)
        return response

class AdminLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data
            user = CustomUser.objects.filter(username=request.data['username']).first()
            if user and not (user.is_staff or user.is_superuser):
                return Response({'error': 'No tienes permiso para acceder a esta área'}, status=status.HTTP_403_FORBIDDEN)
        return response