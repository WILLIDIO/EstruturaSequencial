# -*- coding: utf-8 -*-

"""
    13 - Tendo como dado de entrada a altura (h) de uma pessoa,
    construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""

#peso ideal para homens tomando como base apenas a altura
def pesoMulher (altura):
    calculo = float((62.1*altura) - 44.7)
    return calculo

#peso ideal para mulheres tomando como base apenas a altura
def pesoHomem (altura):
    calculo = float((72.7*altura) - 58)
    return calculo


#Testando
sexo = input("\nVocê é homem (digite h) ou mulher (digite m)? ")
if sexo == "h" or sexo == "H":
    altura = float(input("\nDigite sua altura (exemplo: 1.75 ou 1.60): "))
    print ("\nSeu peso ideal é: %.2f" % pesoHomem(altura))
elif sexo == "m" or sexo == "M":
    altura = float(input("\nDigite sua altura (exemplo: 1.75 ou 1.60): "))
    print ("\nSeu peso ideal é: %.2f" % pesoMulher(altura))
else:
    print ("\nDigite o sexo corretamente\n")