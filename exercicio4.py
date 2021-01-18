# -*- coding:utf-8 -*-

# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média anual.

# Função que retorna uma lista contendo as médias dos bimestres pro ano inteiro
def bimestres ():
    mediasDosBimestres = []
    for i in range (6):
        print ("\nBimestre", i+1, "\n")
        notasBimestre = []
        for i in range (4):
            nota = int(input("Digite uma nota: "))
            notasBimestre.append(nota)
        mediaBimestre = calculaMedia(notasBimestre)
        mediasDosBimestres.append(mediaBimestre)
    return mediasDosBimestres

#Função que recebe uma lista e calcula sua média
def calculaMedia (notas):
    media = float(sum(notas)/len(notas))
    return media

#Chamada das funções
mediaAnual = bimestres()
print ("\nMédia anual", calculaMedia(mediaAnual), "\n")
