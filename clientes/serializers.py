from rest_framework import serializers
from .models import Cliente
from .validators import cpf_valido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        """Verifica se o cpf tem 11 digitos e se é numérico"""
        if not cpf_valido(cpf):
            raise serializers.ValidationError('O numero de cpf é invalido')

        return cpf
    
    def validate_nome(self, nome):
        """
        Docstring for valida_nome
        Verifica se o nome contém somente números
        """

        if any(char.isdigit() for char in nome):
            raise serializers.ValidationError('Não inclua números nessa campo! ')
        
        return nome