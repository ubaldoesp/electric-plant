# Generated by Django 3.2.12 on 2022-03-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipodispositivo', models.IntegerField(choices=[(0, 'Celda'), (1, 'Aerogenerador'), (2, 'Turbina Hidroelectrica')])),
                ('potencia_actual', models.FloatField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'Operacion'), (1, 'Mantenimiento')])),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
