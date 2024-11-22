# productos/views.py
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import DoorWindow, Furniture, BaseProduct
from .serializers import ProductDetailSerializer, FurnitureDetailSerializer
from .models import DoorWindow, Furniture
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import (
    DoorWindowPriceCalculationSerializer, 
    FurniturePriceCalculationSerializer,
    ProductDoorCreateSerializer,
    ProductWindowCreateSerializer,
    ProductFurnitureCreateSerializer,
    ProductDetailSerializer,
    FurnitureDetailSerializer
)
from .pricing import (
    calcular_precio_puerta,
    calcular_precio_ventana,
    calcular_precio_mueble
)

# Vistas de cálculo de precio (estas ya existen)
class CalcularPrecioPuertaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DoorWindowPriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_puerta(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalcularPrecioVentanaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DoorWindowPriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_ventana(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalcularPrecioMuebleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FurniturePriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_mueble(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vistas de creación de productos
class ProductDoorCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductDoorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductWindowCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductWindowCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductFurnitureCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductFurnitureCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        product_id = self.kwargs['product_id']
        
        # Revisa primero si es un mueble
        furniture = Furniture.objects.filter(product_id=product_id).first()
        if furniture:
            return FurnitureDetailSerializer
        
        # Si no es mueble, asume que es puerta/ventana
        doorwindow = DoorWindow.objects.filter(product_id=product_id).first()
        if doorwindow:
            return ProductDetailSerializer
        
        # Si no se encuentra, usa el serializador por defecto
        return ProductDetailSerializer

    def get_object(self):
        product_id = self.kwargs['product_id']
        
        # Primero busca en Furniture
        furniture = Furniture.objects.filter(product_id=product_id).first()
        if furniture:
            return furniture
        
        # Luego busca en DoorWindow
        doorwindow = DoorWindow.objects.filter(product_id=product_id).first()
        if doorwindow:
            return doorwindow
        
        # Si no se encuentra, lanza un error
        raise NotFound(detail="Producto no encontrado")