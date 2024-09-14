from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import ClientRegistrationSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import AdminUserSerializer
from .models import CustomUser


class ClientRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ClientRegistrationSerializer
    permission_classes = [AllowAny]

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_staff=True)  # Filtramos solo administradores
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]