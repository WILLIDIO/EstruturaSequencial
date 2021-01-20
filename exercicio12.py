# -*- coding: utf-8 -*-

"""
	12 - Tendo como dados de entrada a altura de uma pessoa, 
	construa um algoritmo que calcule seu peso ideal, 
	usando a seguinte fórmula: (72.7*altura) - 58
"""


def calculo (altura):
	calculo = int((72.7*altura) - 58)
	return calculo

altura = input("Digite sua altura: ")

print ("Seu peso ideal é: ", calculo(altura))
