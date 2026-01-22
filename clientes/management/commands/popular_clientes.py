from django.core.management.base import BaseCommand
from faker import Faker
from validate_docbr import CPF
from clientes.models import Cliente
import random



class Command(BaseCommand):
    help = 'Popula o banco de dados com dados falsos para teste'

    def handle(self, *args, **kwargs):
        faker = Faker('pt_BR')
        cpf_gerador = CPF()

        self.stdout.write(self.style.WARNING('Iniciando a criação de dados fakes.'))

        for _ in range(50):
            nome = faker.name()
            email = '{}@email.com'.format(nome.lower().replace(' ', ''))
            cpf = cpf_gerador.generate(True) #True para incluir pontuação
            telefone = "{} 9{}-{}".format(
                random.choice(['11', '21', '31', '41']),
                random.randint(1000, 9999),
                random.randint(1000, 9999)
            )

            # Criando objetos no banco de dados

            Cliente.objects.create(
                nome=nome,
                email=email,
                cpf=cpf,
                telefone=telefone
            )
            
        self.stdout.write(self.style.SUCCESS('Sucesso! 50 clientes foram cadastrados.'))
