from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .models import Order
from .serializers import OrderSerializer
from orders.total_price import calculate_total_price  # Asegúrate de que esta importación sea correcta
from deliveries.models import Delivery
from employees.models import Employee
from products.models import DoorWindow, Furniture  # Importa los modelos específicos

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

            # Obtener el empleado
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
