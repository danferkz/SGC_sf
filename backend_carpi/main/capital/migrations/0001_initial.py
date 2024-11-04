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
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Capital',
                'verbose_name_plural': 'Capital',
                'db_table': 'capital',
            },
        ),
    ]
