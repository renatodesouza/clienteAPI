import re

def cpf_valido(numero_cpf):
    """
    Docstring for cpf_valido
    
    :param numero_cpf: Verifica se um CPF é valida seguindo a lógica matemática
    """

    cpf = ''.join(filter(str.isdigit, numero_cpf))

    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * len(cpf):
        return False
    
    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    digito_1 = (soma * 10) % 11
    if digito_1 == 10:
        digito_1 = 0

    if digito_1 != int(cpf[9]):
        return False
    
    # Calculo do segundo digito
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    digito_2 = (soma * 10) % 11
    if digito_2 == 10:
        digito_2 = 0

    if digito_2 != int(cpf[10]):
        return False
    
    return True
