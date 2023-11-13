# tarea_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('', include(router.urls)),
]