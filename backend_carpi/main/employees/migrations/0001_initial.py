from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.DateField(verbose_name='Fecha de Contratación')),
                ('specialty', models.CharField(max_length=100, verbose_name='Especialidad')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está Activo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'employees',
                'ordering': ['hire_date'],
            },
        ),
    ]
