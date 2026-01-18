from django.shortcuts import render

from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    '''
    Docstring for ClienteViewSet
    Exibe, cria, atualiza e deleta clientes.
    '''

    queryset = Cliente.objects.all().order_by('-criado_em')
    serializer_class = ClienteSerializer