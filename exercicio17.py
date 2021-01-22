# -*- coding:utf-8 -*-

"""
    17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o 
    tamanho em metros quadrados da área a ser pintada. Considere que a 
    cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
    que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
    ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os 
    respectivos preços em 3 situações:
        comprar apenas latas de 18 litros;
        comprar apenas galões de 3,6 litros;
        misturar latas e galões, de forma que o desperdício de tinta 
        seja menor. Acrescente 10% de folga e sempre arredonde os 
        valores para cima, isto é, considere latas cheias.
    
    @author: William Lídio
    @email: william.lidio19@gmail.com
"""
# Importando uma função do python que arredonda valores para cima
from math import ceil

area = int (input("\nDigita a área a ser pintada em m²: "))

# Cálculo dos litros
litros = area / 6
print ("\nQuantidade de litros: %.2f" % litros)

# Cálculo das latas e galões
latas = (litros / 18)
galoes = litros / 3.6

# Calculando os preços
valorLatas = ceil (latas) * 80
valorGaloes = ceil (galoes) * 25

print ("\n---Situação 1 e 2---\n")
print ("Quantidade em latas: %.2f" % latas)
print ("Quantidade em galões: %.2f" % galoes)
# Imprimindo os preços
print ("Preço das latas %.2f" % valorLatas)
print ("Preço dos galões %.2f" % valorGaloes)

resultado = valorLatas + (ceil(latas/5)*25)

print ("\n---Situação 3---\n")
# Dica 3.6 multiplicado por 5 dá 18
print ("Você precisará de... ")
print ("Quantidade de latas %.2f" % latas)
print ("Quantidade de galões %d" % ceil(latas/5))
print ("Isso custará ao todo: ", resultado, "R$ \n")

