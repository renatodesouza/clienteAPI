from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        """Verifica se o cpf tem 11 digitos e se é numérico"""
        if len(cpf) != 11:
            raise serializers.ValidationError('O cpf deve ter exatamente 11 digitos')
        
        if not cpf.isdigit():
            raise serializers.ValidationError('O cpf deve conter apenas números')

        return cpf