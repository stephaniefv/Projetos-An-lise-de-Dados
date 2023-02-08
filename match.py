##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto Individual 1 - Módulo 2 - Deu Match!                  #
#  !/usr/bin/env python3                                         #
#  -*- coding: utf-8 -*-                                         #
#  Criado por: Stephanie Ferreira Vale                  #
#  Data de criação: 07/02/2023                                   #
#  versão = '3.11(64-bit)'                                       #
##################################################################
#
# Atividade:
#
# Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade
# de um candidato com uma vaga de acordo com seu resultado nas etapas do
# processo seletivo.
# Para isso foi criado um teste que devolve uma string no seguinte formato:
# eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em
# uma das etapas do processo - entrevista, teste teórico, teste prático e
# avaliação de soft skills).
#
# Criar com Python uma lista para armazenar esses resultados
# (e outros resultados que quiser no mesmo formato; o código
# precisa funcionar para qualquer lista que seja inserida nesse
# formato) e depois uma função que busca o candidato de
# acordo com os critérios digitados pelo usuário.
#

def add_cand(): 

    sair = "sim" 

    while sair != "não": 

        print("Nome do candidato:") 

        cand = input() 

        print("Nota da entrevista:") 

        e = int(input()) 

        print("Nota da avaliação teórica:") 

        t = int(input()) 

        print("Nota da avaliação prática:") 

        p = int(input()) 

        print("Nota da avaliação de soft skills:") 

        s = int(input()) 

        selecao.append([cand, f"e{e}_t{t}_p{p}_s{s}"]) 

        print("Deseja incluir mais? sim ou não") 

        sair = input() 

 

selecao = [] 

add_cand() 

print(selecao) 