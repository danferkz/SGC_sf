# employees/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.models import CustomUser
from .models import Employee
from .serializers import EmployeeSerializer
from users.views import IsAdminUser

class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            user = get_object_or_404(
                CustomUser, 
                id=serializer.validated_data['user_id']
            )
            
            # Crear el empleado
            employee = Employee.objects.create(
                user=user,
                hire_date=serializer.validated_data['hire_date'],
                specialty=serializer.validated_data['specialty'],
                is_active=serializer.validated_data.get('is_active', True)
            )
            
            # Devolver los datos del empleado creado
            return Response(
                EmployeeSerializer(employee).data,
                status=status.HTTP_201_CREATED
            )
            
        except serializers.ValidationError as e:
            return Response(
                {'detail': e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )