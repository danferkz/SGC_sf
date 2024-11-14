# products/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from .serializers import (
    DoorPriceCalculationSerializer, 
    WindowPriceCalculationSerializer, 
    FurniturePriceCalculationSerializer,
    ProductDoorCreateSerializer,
    ProductFurnitureCreateSerializer,
    ProductWindowCreateSerializer
)
from .pricing import (
    calcular_precio_puerta,
    calcular_precio_ventana,
    calcular_precio_mueble
)

# 1. Calcula el precio de una puerta
class CalcularPrecioPuertaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DoorPriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_puerta(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. Calcula el precio de una ventana
class CalcularPrecioVentanaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WindowPriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_ventana(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 3. Calcula el precio de un mueble
class CalcularPrecioMuebleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FurniturePriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_mueble(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# 4. Validar que el usuario sea un cliente
# products/views.py
def validate_is_cliente(user):
    if not user.is_client:
        raise PermissionDenied("You do not have permission to perform this action.")

# 5. Crear un producto de tipo puerta
class ProductDoorCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        validate_is_cliente(request.user)
        serializer = ProductDoorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 6. Crear un producto de tipo mueble
class ProductWindowCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        validate_is_cliente(request.user)
        serializer = ProductWindowCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 7. Crear un producto de tipo ventana
class ProductFurnitureCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        validate_is_cliente(request.user)
        serializer = ProductFurnitureCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)