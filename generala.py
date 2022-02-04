# -*- coding: utf-8 -*-
# Ejercicio 5.2
# Código realizado tras la explicación del docente Matías López
import random

def tirar(cant_dados):
    return [ random.randint(1,6) for _ in range(cant_dados)]

def es_generala(dados):
    return dados.count(dados[0]) == 5

def cuantos_de_cada(dados_en_mesa):
    return sorted([(dados_en_mesa.count(d),d) for d in range(1,6 + 1)], reverse=True)

def generala_en_varias_manos():
    manos = 3
    mesa = []
    
    for i in range(manos):
        mesa = mesa + tirar(5 - len(mesa))
        if i < manos - 1:
            (cant, valor) = cuantos_de_cada(mesa) [0]
            mesa = [valor] * cant
    return es_generala(mesa)


n_tiradas = 100000

ganadas = sum([generala_en_varias_manos() for _ in range(n_tiradas)])

probabilidad = ganadas / n_tiradas


