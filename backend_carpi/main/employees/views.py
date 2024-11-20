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

# listar empleados
class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Employee.objects.all()
    

# actualizar datos de un empleado
class EmployeeUpdateView(generics.UpdateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Employee.objects.all()
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            employee = self.get_object()
            
            # Actualizar solo los datos de specialty y is_active
            employee.specialty = serializer.validated_data.get(
                'specialty', employee.specialty
            )
            employee.is_active = serializer.validated_data.get(
                'is_active', employee.is_active
            )
            employee.save()
            
            # Devolver los datos del empleado actualizado
            return Response(
                EmployeeSerializer(employee).data,
                status=status.HTTP_200_OK
            )
            
        except serializers.ValidationError as e:
            return Response(
                {'detail': e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
