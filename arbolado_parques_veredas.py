# -*- coding: utf-8 -*-
# Ejercicio 8.9
import os
import pandas as pd
import seaborn as sns

directorio = '../Data'
archivo_vereda = 'arbolado-publico-lineal-2017-2018.csv'
archivo_parque = 'arbolado-en-espacios-verdes.csv'
    
#%% Abrí ambos datasets a los que llamaremos df_parques y df_veredas
fname_ved = os.path.join(directorio, archivo_vereda)
df_veredas = pd.read_csv(fname_ved)

fname_par = os.path.join(directorio, archivo_parque)
df_parques = pd.read_csv(fname_par)

#%% Para cada dataset armate otro seleccionando solamente las filas correspondientes a las tipas (llamalos df_tipas_parques y df_tipas_veredas, respectivamente) y las columnas correspondientes al diametro a la altura del pecho y alturas

col_par = ['altura_tot', 'diametro', 'nombre_cie']
col_ver = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']

esp_par = 'Tipuana Tipu'
esp_ver = 'Tipuana tipu'

df_col_par = df_parques[col_par]
df_col_ver = df_veredas[col_ver]


df_tipas_parques = df_col_par[df_col_par['nombre_cie'] == esp_par].copy()

df_tipas_veredas = df_col_ver[df_col_ver['nombre_cientifico'] == esp_ver].copy()

# Renombro altura_tot en parques y diametro_altura_pecho en veredas
df_tipas_parques = df_tipas_parques.rename(columns = {'altura_tot': 'altura', 'diametro': 'diametro_altura_pecho'})
df_tipas_veredas = df_tipas_veredas.rename(columns = {'altura_arbol': 'altura'})


# Agregale a cada dataframe (df_tipas_parques y df_tipas_veredas) una columna llamada 'ambiente' que en un caso valga siempre 'parque' y en el otro caso 'vereda'.

df_tipas_parques = df_tipas_parques.assign(ambiente= 'parque')
df_tipas_veredas = df_tipas_veredas.assign(ambiente= 'vereda')

# Juntar ambos datasets
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# Creá un boxplot para los diámetros a la altura del pecho de la tipas distinguiendo los ambientes
df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')

df_tipas.boxplot('altura',by = 'ambiente')

