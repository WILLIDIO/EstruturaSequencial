# -*- coding:utf-8 -*-

#   8 - Faça um Programa que pergunte quanto você ganha por hora e o 
#   número de horas trabalhadas no mês. Calcule e mostre o 
#   total do seu salário no referido mês.

valorHora = int(input("Quanto você ganha por hora? "))

horasMes = int(input("Quantas horas trabalhadas no mês? "))

salario = valorHora * horasMes

print ("Salário: R$", salario)