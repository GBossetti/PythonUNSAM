# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

#Ejercicio 1.7
# =============================================================================
# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# 
# while saldo > 0:
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual
# 
# print('Total pagado', round(total_pagado, 2))
# =============================================================================

#Ejercicio 1.8
# =============================================================================
# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# mes= 0
# 
# while saldo > 0:
#     if mes < 12:
#         saldo = saldo * (1+tasa/12) - (pago_mensual + 1000)
#         total_pagado = total_pagado + (pago_mensual + 1000)
#         mes+=1
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual
#         mes+=1
#         
# print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses')
# =============================================================================

#Ejercicio 1.9
# =============================================================================
# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# mes= 0
# 
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000
# 
# while saldo > 0:
#     if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
#         saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
#         total_pagado = total_pagado + (pago_mensual + pago_extra)
#         mes+=1
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual
#         mes+=1
#         
# print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses')
# =============================================================================

#Ejercicio 1.10
# =============================================================================
# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# mes= 0
# 
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000
# 
# while saldo > 0:
#     if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
#         saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
#         total_pagado = total_pagado + (pago_mensual + pago_extra)
#         mes+=1
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual
#         mes+=1
#     print(mes, round(total_pagado, 2), round(saldo, 2))    
#         
# print('Total pagado', round(total_pagado, 2))
# print('Meses:', mes)
# =============================================================================

#Ejercicio 1.11
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes= 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        total_pagado = total_pagado + (pago_mensual + pago_extra)
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    
    mes+=1
    print(mes, round(total_pagado, 2), round(saldo, 2))    
        
print('Total pagado', round(total_pagado, 2))
print('Meses:', mes)
