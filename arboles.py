# -*- coding: utf-8 -*-
#Ejercicio 4.18
def leer_arboles(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding = 'utf-8')
    rows = csv.reader(f)
    headers = next(rows)
    arboleda = []
    arboleda = [{name: tree for name, tree in zip(headers, row)} for row in rows]
    return arboleda
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')


#Ejercicio 4.19
h=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(H)

#Ejercicio 4.20
h_and_d = [ (float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(h_and_d)

#Ejercicio 4.21
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    diccio = {}
    #alt_dia = []
    for especie in especies:
        alt_diam = [ (float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
        diccio[especie] = alt_diam
    return diccio            

print(diccio_med=medidas_de_especies(especies, arboleda))
