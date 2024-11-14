# Generated by Django 5.1.2 on 2024-11-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(verbose_name='Fecha de Entrega')),
                ('delivery_notes', models.TextField(blank=True, verbose_name='Notas de Entrega')),
                ('signature_received', models.BooleanField(default=False, verbose_name='Firma Recibida')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entregas',
                'db_table': 'deliveries',
            },
        ),
    ]
