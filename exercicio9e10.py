# -*- coding:utf-8 -*-

"""
    9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
    temperatura em graus Celsius. C = 5 * ((F-32) / 9).

    # 10 - Faça um Programa que peça a temperatura em graus Celsius,
    transforme e mostre em graus Fahrenheit
"""


def celsiusParaFahren(celsius):
    fahren = float(((celsius * 9) / 5) + 32)
    return fahren


def fahrenParaCelsius(fahren):
    celsius = float(((fahren - 32) * 5) / 9)
    return celsius


# Testando as funções
tempc = float(input("Digite a temperatura em graus celsius: "))
print(celsiusParaFahren(tempc))

tempf = float(input("Digite a temperatura em graus fahrenheit: "))
print(fahrenParaCelsius(tempf))

