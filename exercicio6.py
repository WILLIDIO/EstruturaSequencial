# -*- coding:utf-8 -*-

# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

diametro = float (input("Digite o diâmetro do círculo em cm: "))

raio = diametro / 2

print ("Raio: ", raio)

pi = 3.14
area = pi * (raio**2)

print ("Área da circunferência: ", area, "cm²")
