# -*- coding: utf-8 -*-

"""
	12 - Tendo como dados de entrada a altura de uma pessoa, 
	construa um algoritmo que calcule seu peso ideal, 
	usando a seguinte fórmula: (72.7*altura) - 58
"""


def calculo (altura):
	calculo = float((72.7*altura) - 58)
	return calculo

print ("Use ponto (.) para separar, exemplo: 1.75 ou 1.80")
altura = float(input("Digite sua altura em metros: "))

#Fiz uma interpolação de strings para mostrar resultado resumido
print ("Seu peso ideal é: %.2f" % calculo(altura))
