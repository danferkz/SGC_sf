# Generated by Django 5.1.2 on 2024-11-14 07:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deliveries', '0001_initial'),
        ('employees', '0002_initial'),
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(limit_choices_to={'is_client': True}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='deliveries.delivery', verbose_name='Entrega'),
        ),
        migrations.AddField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.employee', verbose_name='Empleado'),
        ),
    ]
