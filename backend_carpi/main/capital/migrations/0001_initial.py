# Generated by Django 5.1.1 on 2024-10-02 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_disponible', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
