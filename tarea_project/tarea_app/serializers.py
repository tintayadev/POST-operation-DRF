from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__' # Tambien podemos especificar como ['nombre', 'descripcion'] pero __all__ incluye a todos.
