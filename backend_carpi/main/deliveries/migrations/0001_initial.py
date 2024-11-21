# Generated by Django 5.1.1 on 2024-11-19 01:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(verbose_name='Fecha de Entrega')),
                ('delivery_notes', models.TextField(blank=True, verbose_name='Notas de Entrega')),
                ('signature_received', models.BooleanField(default=False, verbose_name='Firma Recibida')),
                ('delivery_option', models.BooleanField(default=False, verbose_name='Opción de Entrega')),
                ('additional_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo Adicional')),
                ('door_window', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='products.doorwindow')),
                ('furniture', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='products.furniture')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entregas',
                'db_table': 'deliveries',
            },
        ),
    ]
