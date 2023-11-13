from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import TareaSerializer
from .models import Tarea

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    @action(detail=False, methods=['GET'])
    def obtener_tareas_limpieza(self, request):
        tareas_limpieza = Tarea.objects.filter(nombre="Limpieza")
        serializer = self.get_serializer(tareas_limpieza, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'])
    def crear_tarea_personalizada(self, request):
        # Asumiendo que los datos de la nueva tarea se envían en el cuerpo de la solicitud.
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        else:
            return Response(serializer.errors, status=400)  # 400 Bad Request