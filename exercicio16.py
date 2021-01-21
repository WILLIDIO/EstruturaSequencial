# -*- coding: utf-8 -*-

"""
    16 - Faça um programa para uma loja de tintas. O programa deverá pedir 
    o tamanho em metros quadrados da área a ser pintada. Considere que a 
    cobertura da tinta é de 1 litro para cada 3 metros quadrados e que 
    a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
    Informe ao usuário a quantidades de latas de tinta a serem 
    compradas e o preço total.
"""

tamanhoDaArea = int(input("Digita a área a ser pintada em m²: "))

quantidadeLitros = int(tamanhoDaArea/3)

quantidadeLatas = quantidadeLitros / 18

valor = quantidadeLatas * 80

print ("Quantidade de litros por metros: ", quantidadeLitros)
print ("Quantidade de latas a ser compradas: ", quantidadeLatas)
print ("Valor a ser pago: ", valor, " R$")