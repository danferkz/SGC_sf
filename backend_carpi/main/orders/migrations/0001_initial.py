# Generated by Django 5.1.1 on 2024-10-15 22:59

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
                ('entrega_domicilio', models.BooleanField(default=False)),
                ('estado', models.CharField(default='pendiente', max_length=20)),
            ],
        ),
    ]
