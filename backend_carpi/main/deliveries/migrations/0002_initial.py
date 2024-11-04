import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deliveries', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='delivered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.employee', verbose_name='Entregado Por'),
        ),
    ]
