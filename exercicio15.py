# -*- coding: utf-8 -*-

"""
    15 - Faça um Programa que pergunte quanto você ganha por hora e o número de 
    horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
    referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
    8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário 
    bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. 
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
        Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

ganhoHora = int(input("Digite quanto ganha por hora: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = ganhoHora * horasTrabalhadas
ir = salarioBruto * (11/100)
inss = salarioBruto * (8/100)
sindicato = salarioBruto * (5/100)
salarioLiquido = salarioBruto - ir - inss - sindicato

print ("Salário bruto", salarioBruto, " R$")
print ("IR 11%")
print ("IINSS 8%")
print ("Sindicato 5%")
print ("Salário Líquido", salarioLiquido, " R$")

