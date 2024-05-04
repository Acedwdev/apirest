from .models import Empleados
from rest_framework import serializers

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ['id', 'identificacion', 'nombre', 'apellidos', 'correo','salario_base', 'activo']
        # fields = ['identificacion', 'nombre', 'apellidos', 'correo','salario_base', 'activo']
        # read_only_fields = ('id', 'nombre', 'apellidos', 'correo', 'salario_base', 'activo)


