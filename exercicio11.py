# -*- coding: utf-8 -*-

"""
	11 - Faça um Programa que peça 2 números inteiros e um número real.
		 Calcule e mostre:
		 o produto do dobro do primeiro com metade do segundo.
		 a soma do triplo do primeiro com o terceiro.
		 o terceiro elevado ao cubo.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

produto = (numero1*2)*(numero2/2)
soma = (numero1*3)+numero3
cubo = numero3**3

"""
Teste
numero1 = 10
nuemro2 = 10
numero3 = 10

Saídas esperadas
Produto: 100
Soma: 40
Cubo: 1000
"""

print ("Produto: ", produto)
print ("Soma: ", soma)
print ("Cubo: ",cubo)

