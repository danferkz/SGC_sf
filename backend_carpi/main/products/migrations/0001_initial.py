# Generated by Django 5.1.1 on 2024-09-09 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('numero_producto', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_madera', models.CharField(max_length=50)),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('barnizado', models.BooleanField(default=False)),
                ('productor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('producto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.producto')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=7)),
                ('nombre_pieza', models.CharField(max_length=100)),
                ('parte_juego', models.BooleanField(default=False)),
            ],
            bases=('products.producto',),
        ),
        migrations.CreateModel(
            name='Puerta',
            fields=[
                ('producto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.producto')),
                ('largo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cantidad_hojas', models.IntegerField()),
                ('exterior', models.BooleanField(default=False)),
            ],
            bases=('products.producto',),
        ),
        migrations.CreateModel(
            name='Ventana',
            fields=[
                ('producto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.producto')),
                ('largo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cantidad_hojas', models.IntegerField()),
                ('exterior', models.BooleanField(default=False)),
            ],
            bases=('products.producto',),
        ),
    ]
