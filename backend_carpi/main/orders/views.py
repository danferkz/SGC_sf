from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order
from .serializers import OrderSerializer, OrderupdateSerializer
from orders.total_price import calculate_total_price  # Asegúrate de que esta importación sea correcta
from deliveries.models import Delivery
from employees.models import Employee
from products.models import DoorWindow, Furniture  # Importa los modelos específicos
from users.views import BaseAuthenticatedView, IsAdminUser
from uuid import UUID

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            product_id = request.data.get("product")  # ID del producto
            delivery_id = request.data.get("delivery")  # ID de la entrega
            employee_id = request.data.get("employee")  # ID del empleado

            try:
                # Primero intenta obtener el producto como DoorWindow
                product = DoorWindow.objects.get(pk=product_id)
                cost_price = product.cost_price

            except DoorWindow.DoesNotExist:
                # Si no se encuentra como DoorWindow, intenta obtenerlo como Furniture
                try:
                    product = Furniture.objects.get(pk=product_id)
                    cost_price = product.cost_price
                except Furniture.DoesNotExist:
                    return Response(
                        {"error": "Product not found"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            # Obtener el costo adicional de entrega
            try:
                delivery = Delivery.objects.get(pk=delivery_id)
                additional_cost = delivery.additional_cost
            except Delivery.DoesNotExist:
                return Response(
                    {"error": "Delivery not found"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Obtener el empleado si se proporciona un ID
            employee = None
            if employee_id:
                try:
                    employee = Employee.objects.get(pk=employee_id)
                except Employee.DoesNotExist:
                    return Response(
                        {"error": "Employee not found"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            # Calcular el precio total usando la función de utils
            total_price = calculate_total_price(cost_price, additional_cost)

            # Crear la orden y guardar el total calculado
            order = serializer.save(
                client=request.user,
                employee=employee,
                delivery=delivery,
                total_price=total_price
            )
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListAPIViewAdmin(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Order.objects.all()
    

class UpdateOrderAPIAdmin(BaseAuthenticatedView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request, *args, **kwargs):
        order_id = kwargs.get("pk")
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderUpdateAPIView(BaseAuthenticatedView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def patch(self, request, *args, **kwargs):
        order_id = kwargs.get("pk")
        try:
            UUID(str(order_id))  # Validar el formato UUID
            order = Order.objects.get(pk=order_id)
        except (ValueError, Order.DoesNotExist):
            return Response(
                {"error": "Invalid order ID or order not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verificar si el cliente que realiza la solicitud es el mismo que hizo el pedido
        if order.client != request.user:
            return Response(
                {"error": "You are not authorized to perform this action"},
                status=status.HTTP_403_FORBIDDEN
            )

        # Crear un serializer con el objeto existente y los datos de la solicitud
        serializer = OrderupdateSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            # Guardar los cambios en el estado
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListAPIViewCliente(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)
