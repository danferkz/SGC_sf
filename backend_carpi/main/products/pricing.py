# products/pricing.py
from decimal import Decimal

def calcular_precio_base(data):
    # Precio base según el tipo de madera
    wood_prices = {
        'Pino': Decimal('100.00'),
        'Roble': Decimal('150.00'),
        'Caoba': Decimal('200.00'),
        'Cedro': Decimal('180.00'),
        # Añadir más tipos de madera según sea necesario
    }
    
    base_price = wood_prices.get(data['wood_type'], Decimal('100.00'))
    
    if data['is_varnished']:
        base_price += Decimal('50.00')
    return base_price

def calcular_precio_puerta(data):
    price = calcular_precio_base(data)
    # Cálculo basado en dimensiones
    area = Decimal(str(data['length'])) * Decimal(str(data['width']))
    price += (area * Decimal('0.05'))  # 0.05 por unidad de área
    
    # Ajuste por número de hojas
    price += (Decimal(str(data['number_of_sheets'])) * Decimal('50.00'))
    
    price *= Decimal('1.07')  # +7% para puertas
    if data['is_exterior']:
        price *= Decimal('1.02')  # +2% si es exterior
    
    return round(price, 2)

def calcular_precio_ventana(data):
    price = calcular_precio_base(data)
    # Cálculo basado en dimensiones
    area = Decimal(str(data['length'])) * Decimal(str(data['width']))
    price += (area * Decimal('0.03'))  # 0.03 por unidad de área
    
    # Ajuste por número de hojas
    price += (Decimal(str(data['number_of_sheets'])) * Decimal('30.00'))
    
    price *= Decimal('1.05')  # +5% para ventanas
    if data['is_exterior']:
        price *= Decimal('1.02')  # +2% si es exterior
    
    return round(price, 2)

def calcular_precio_mueble(data):
    price = calcular_precio_base(data)
    # Cálculo basado en peso
    weight = Decimal(str(data['weight']))
    price += (weight * Decimal('0.1'))  # 0.1 por unidad de peso
    
    price *= Decimal('1.10')  # +10% para muebles
    
    # Descuento por peso
    weight_discount = (weight // 1000) * Decimal('0.01')
    if weight_discount > 0:
        price *= (1 - weight_discount)
    
    # Ajuste si es parte de un set
    if data['is_part_of_set']:
        price *= Decimal('0.95')  # 5% de descuento por ser parte de un set
    
    return round(price, 2)