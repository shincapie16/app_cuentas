from rest_framework import viewsets
from . serializer import *
from . models import *

class RegistroView(viewsets.ModelViewSet):
    serializer_class = RegistroSerializer
    queryset = Registro.objects.all()


class CategoriaView(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()