from rest_framework import viewsets, permissions
from .models import Empleados
from .serializers import EmpleadosSerializer

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadosSerializer