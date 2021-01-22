# -*- coding:utf-8 -*-

"""
    18 - Faça um programa que peça o tamanho de um arquivo para download 
    (em MB) e a velocidade de um link de Internet (em Mbps), 
    calcule e informe o tempo aproximado de download do 
    arquivo usando este link (em minutos).
"""

arquivo = float (input("Digite o tamanho em MB: "))

#Velocidade do link é dada em mega bit
link = float(input("Digite a velocidade do link em Mbps: "))

# 8 bits representam um byte
tempo = float(arquivo / (link/8))

# O tempo está em segundos, por isso dividimos por 60 para ter os minutos
print (("Tempo de download: %.2f minutos") % (tempo/60))
