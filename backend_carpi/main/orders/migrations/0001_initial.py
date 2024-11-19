# Generated by Django 5.1.1 on 2024-11-19 18:37

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
                ('orders_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('in_progress', 'En Progreso'), ('completed', 'Completado'), ('delivered', 'Entregado'), ('cancelled ', 'Cancelado')], default='pending', max_length=20, verbose_name='Estado')),
                ('promised_date', models.DateField(verbose_name='Fecha Prometida')),
                ('total_price', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Precio Total')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'orders',
            },
        ),
    ]
