import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoorWindow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('wood_type', models.CharField(max_length=100, verbose_name='Tipo de Madera')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de Costo')),
                ('is_varnished', models.BooleanField(default=False, verbose_name='Es Barnizado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('product_type', models.CharField(choices=[('door', 'Puerta'), ('window', 'Ventana')], max_length=6, verbose_name='Tipo de Producto')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Longitud')),
                ('width', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ancho')),
                ('is_exterior', models.BooleanField(default=False, verbose_name='Es Exterior')),
                ('number_of_sheets', models.IntegerField(verbose_name='Número de Hojas')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produced_%(class)s', to='employees.employee', verbose_name='Productor')),
            ],
            options={
                'verbose_name': 'Puerta/Ventana',
                'verbose_name_plural': 'Puertas/Ventanas',
                'db_table': 'doors_windows',
            },
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('wood_type', models.CharField(max_length=100, verbose_name='Tipo de Madera')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de Costo')),
                ('is_varnished', models.BooleanField(default=False, verbose_name='Es Barnizado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('piece_name', models.CharField(max_length=100, verbose_name='Nombre de la Pieza')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Peso')),
                ('is_part_of_set', models.BooleanField(default=False, verbose_name='Es Parte de un Conjunto')),
                ('set_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del Conjunto')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produced_%(class)s', to='employees.employee', verbose_name='Productor')),
            ],
            options={
                'verbose_name': 'Mueble',
                'verbose_name_plural': 'Muebles',
                'db_table': 'furniture',
            },
        ),
    ]
