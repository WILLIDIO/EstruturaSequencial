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
"""

area = float (input("Digita a área a ser pintada em m²: "))

litros = area / 6

latas = (litros / 18)
print ("Latas ", latas)
galoes = litros / 3.6
print ("Galoes ", galoes)



valorLatas = latas * 80
valorGaloes = galoes * 25

print ("\nQuantidade de litros necessários: %.2f litros" % litros)

#situação 1 - comprar apenas latas
print ("\nSão necessárias %.2f de lata(s)" % latas)
print ("\nPreço R$ %.2f" % valorLatas)

#situação 2 - comprar apenas galões de tinta
print ("\nSão necessárias %.2f de galão(ões)" % galoes)
print ("\nPreço R$ %.2f" % valorGaloes)

#Para evitar desperdício

"""
tamanho = float(input('Entre com o tamanho da área: '))

litros = tamanho / 6
latas = litros / 18

if(latas % 18 !=0):
    latas += 1
preco = latas * 80

galoes = litros / 3.6
if (galoes % 3.6 != 0):
    galoes += 1
preco2 = galoes * 25

#mistura de latas e galoes
misturaL = int(litros / 18.0)
misturaG = int((litros - (misturaL * 18)) / 3.6)

if ((litros - (misturaL * 18) % 3.6 != 0)):
    misturaG += 1

print('Apenas latas de 18 litros: %d' % latas)
print('Apenas galões de 3.6 litros: %d' % galoes)
print('Mistura: %d latas e %d galoes = %.2f' % (misturaL, misturaG, ((misturaL * 80) + (misturaG * 25))))
"""