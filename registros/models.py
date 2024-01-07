from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length = 25)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]
    METODO_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta_credito', 'Tarjeta de Crédito'),
        ('tarjeta_debito', 'Tarjeta de Débito'),
        ('transferencia', 'Transferencia'),
        ('cheque', 'Cheque')
        ]

    titulo = models.CharField(max_length=75)
    descripcion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_registro = models.CharField(choices=TIPO_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True, blank=True)
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    metodo_pago = models.CharField(null=True, blank=True,choices=METODO_PAGO_CHOICES)
    numero_comprobante = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titulo
    

