# orders/views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from .total_price import calculate_total_price
from deliveries.models import Delivery
from employees.models import Employee
from products.models import Product  # Asegúrate de que exista un modelo Product con el campo `cost_price`
from rest_framework.permissions import IsAuthenticated

class OrderViewSet(viewsets.ModelViewSet):
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
                # Obtener el precio de costo del producto
                product = Product.objects.get(pk=product_id)
                cost_price = product.cost_price  # Cambiado a cost_price

                # Obtener el costo adicional de entrega
                delivery = Delivery.objects.get(pk=delivery_id)
                additional_cost = delivery.additional_cost

                # Obtener el empleado
                employee = Employee.objects.get(pk=employee_id)
            except (Product.DoesNotExist, Delivery.DoesNotExist, Employee.DoesNotExist):
                return Response(
                    {"error": "Product, Delivery, or Employee not found"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Calcular el precio total usando la función de utils
            total_price = calculate_total_price(cost_price, additional_cost)

            # Crear la orden y guardar `total_price` en la base de datos
            order = serializer.save(
                client=request.user,
                employee=employee,
                delivery=delivery,
                total_price=total_price  # Aquí se guarda el total calculado en la base de datos
            )
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
