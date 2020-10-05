# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:35:04 2020

@author: Gonzalo
"""
cadena = input('Ingrese palabra:')
capadepenapa = ''
for c in cadena:
    if c=='a':
        capadepenapa+= 'apa'
    elif c=='e':
        capadepenapa+= 'epe'
    elif c=='i':
        capadepenapa+= 'ipi'
    elif c=='o':
        capadepenapa+= 'opo'
    elif c=='u':
        capadepenapa+= 'upu'
    else:
        capadepenapa+= c
print(capadepenapa)