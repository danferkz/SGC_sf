# Generated by Django 5.1.1 on 2024-09-09 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('numero_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pactada', models.DateField()),
                ('entrega_domicilio', models.BooleanField(default=False, verbose_name='Entrega a domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
    ]
