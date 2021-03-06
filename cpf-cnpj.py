# Este código é um Fork de Pedro Lucas, GitHub: https://github.com/DoisLucas/
# O projeto original está no seguinte endereço: https://github.com/DoisLucas/ValidacaoCPF-CNPJ-Python

#!/usr/bin/env python3
# encoding: <UTF-8>

print("Este script irá verificar se o CPF/CNPJ são válidos ou não.")
documento = input("Digite um CPF/CNPJ: ")

# Início da verificação do CPF
if documento.__len__() == 11:
    digt1 = 0
    digt2 = 0
    documento = str(documento)

    # Verificando o padrão de CPF invalidos 000.000.000.00, 111.111.111.11...
    counter = 0
    for x in documento:
        if x == documento[1]:
            counter += 1

    # Calculando o primeiro digito verificador
    calculo = int(documento[0]) * 10 + int(documento[1]) * 9 + int(documento[2]) * 8 + int(documento[3]) * 7 + int(
        documento[4]) * 6 + int(documento[5]) * 5 + int(documento[6]) * 4 + int(documento[7]) * 3 + int(
        documento[8]) * 2
    calculo = (calculo * 10) % 11

    if calculo == 10:
        digit1 = 0
    else:
        digit1 = calculo

    # Calculando o segundo digito verificador
    calculo = int(documento[0]) * 11 + int(documento[1]) * 10 + int(documento[2]) * 9 + int(documento[3]) * 8 + int(
        documento[4]) * 7 + int(documento[5]) * 6 + int(documento[6]) * 5 + int(documento[7]) * 4 + int(
        documento[8]) * 3 + digit1 * 2
    calculo = (calculo * 10) % 11

    if calculo == 10:
        digit2 = 0
    else:
        digit2 = calculo

    if (digit1 == int(documento[9])) and (digit2 == int(documento[10]) and counter != 11):
        print('{}.{}.{}-{}'.format(documento[0:3],documento[3:6],documento[6:9],documento[9:11]), 'CPF Válido')
    else:
        print('{}.{}.{}-{}'.format(documento[0:3],documento[3:6],documento[6:9],documento[9:11]),'CPF Inválido')

# Início da verificação do CNPJ
elif documento.__len__() == 14:

    documento = str(documento)

    # Verificando o padrão de CNPJ invalidos  00.000.000/0000-00,  11.111.111/1111-11...
    counter = 0
    for x in documento:
        if x == documento[1]:
            counter += 1

    # Calculando o primeiro digito verificador
    calculo = int(documento[0]) * 5 + int(documento[1]) * 4 + int(documento[2]) * 3 + int(documento[3]) * 2 + int(
        documento[4]) * 9 + int(documento[5]) * 8 + int(documento[6]) * 7 + int(documento[7]) * 6 + int(
        documento[8]) * 5 + int(documento[9]) * 4 + int(documento[10]) * 3 + int(documento[11]) * 2
    calculo = (calculo * 10) % 11

    if calculo == 10:
        digit1 = 0
    else:
        digit1 = calculo

    # Calculando o segundo digito verificador
    calculo = int(documento[0]) * 6 + int(documento[1]) * 5 + int(documento[2]) * 4 + int(documento[3]) * 3 + int(
        documento[4]) * 2 + int(documento[5]) * 9 + int(documento[6]) * 8 + int(documento[7]) * 7 + int(
        documento[8]) * 6 + int(documento[9]) * 5 + int(documento[10]) * 4 + int(documento[11]) * 3 + digit1 * 2
    calculo = (calculo * 10) % 11

    if calculo == 10:
        digit2 = 0
    else:
        digit2 = calculo

    if (digit1 == int(documento[12])) and (digit2 == int(documento[13]) and counter != 14):
        print('{}.{}.{}/{}-{}'.format(documento[0:2],documento[2:5],documento[5:8],documento[8:12],documento[12:14]),'CNPJ Válido')

    else:
        print('{}.{}.{}/{}-{}'.format(documento[0:2],documento[2:5],documento[5:8],documento[8:12],documento[12:14]),'CNPJ Inválido')
