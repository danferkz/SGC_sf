# orders/utils.py
from decimal import Decimal

def calculate_total_price(product_price, additional_cost):
    """
    Calcula el precio total de una orden sumando el precio del producto y el costo adicional de entrega.
    """
    total_price = Decimal(product_price) + Decimal(additional_cost)
    return total_price
