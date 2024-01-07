# Generated by Django 5.0.1 on 2024-01-07 17:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=75)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('tipo_registro', models.CharField(choices=[('ingreso', 'Ingreso'), ('egreso', 'Egreso')])),
                ('cantidad', models.IntegerField()),
                ('metodo_pago', models.CharField(blank=True, choices=[('efectivo', 'Efectivo'), ('tarjeta_credito', 'Tarjeta de Crédito'), ('tarjeta_debito', 'Tarjeta de Débito'), ('transferencia', 'Transferencia'), ('cheque', 'Cheque')], null=True)),
                ('numero_comprobante', models.CharField(blank=True, max_length=50, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registros.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
