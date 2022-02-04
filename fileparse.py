# -*- coding: utf-8 -*-
# Ejercicio 6.9
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        if has_headers:     # Si no se aclara ausencia de headers, el programa realizar un diccionario con los nombres de las columnas del headers, y los datos de cada fila correspondiente
            
            # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
    
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
    
                if types:       # Convierte el tipo de dato 
                    fila = [func(val) for func, val in zip(types, fila)]
    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        
        else:       # Si has_headers = false, el programa crea tuplas con los datos de cada fila
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if types:       # Convierte el tipo de dato 
                    fila = [func(val) for func, val in zip(types, fila)]
                
                # Armar la tupla
                registro = tuple(fila)
                registros.append(registro)

    return registros

precios = parse_csv('C:/Users/Gonzalo/Desktop/PROGRAMACIÓN/UNSAM2021/ejercicios_python/Data/precios.csv', types=[str,float], has_headers=False)



