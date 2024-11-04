import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('in_progress', 'En Progreso'), ('completed', 'Completado'), ('delivered', 'Entregado'), ('cancelled', 'Cancelado')], default='pending', max_length=20, verbose_name='Estado')),
                ('promised_date', models.DateField(verbose_name='Fecha Prometida')),
                ('home_delivery', models.BooleanField(default=False, verbose_name='Entrega a Domicilio')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio por Unidad')),
                ('total_price', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Precio Total')),
            ],
            options={
                'verbose_name': 'Ítem de Pedido',
                'verbose_name_plural': 'Ítems de Pedido',
                'db_table': 'order_items',
            },
        ),
    ]
