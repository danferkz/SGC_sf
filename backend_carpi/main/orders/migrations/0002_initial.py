import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0002_initial'),
        ('orders', '0001_initial'),
        ('products', '0001_initial'),
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
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.employee', verbose_name='Empleado'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order', verbose_name='Pedido'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items_door_window', to='products.doorwindow', verbose_name='Producto (Puerta/Ventana)'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_furniture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items_furniture', to='products.furniture', verbose_name='Producto (Mueble)'),
        ),
    ]
