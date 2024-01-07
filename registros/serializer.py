from rest_framework import serializers
from . models import *

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'