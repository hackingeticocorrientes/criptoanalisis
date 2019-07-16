#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:40:16 2019

@author: Rafael Ernesto Perez

"""

from __future__ import unicode_literals
import operator
from collections import OrderedDict
from math import log10
import mcd
import VigenereAlgoritmo

# caso en que se tenga una cadena separada por sub grupos 
#cadena_cero = "Necvz mesdkee t ectdzr Cjviizrken, Pvgzruammr dz mevdgko wvfqpic, Cjpfsvp p gzrkig edausea Lyv ei xl fmietz wv onxvnoe ln gelrzp! ¡Vmkyaawej a oyj hdnfs qecizrken E jagzrr v pr Pvxiiv s dommi, tp wzei eirjkrnoi ca bpfrde Ueg prumic iwe jizqgrz e teñdv!"
cadena_cero = "GW CCMR4OVRCWIDMU PS 6E RLREI FP LV GTTPESNZG3E S5E DI FPD3GC LL ZWV5D3S FP S3WVPMVW E2IAXQRRVJKNOD GQY E6 JKY DZ IPNO8XTLR YIDTL3HCOED IP WOD WK3TZQC3 Y CSO0EC WW 3E1YTTDVH UTN ZP EZN9GKXIZRVZ DZ MPQOCQCNI9R UPCCIVL  E8 IN WE8KWLJZ RQ 4EXRKNO  DI EZN9GG PSEE R2AXXKNA XSOZ R9QRPR 9 JQ2ZVV GW C9HKRO  VYP1UZ IU4A Z1R2EDMQY T3IPP U8 WKRN3JKNAYS G3PZGKQIXS FPNEVQ OE6 ETROE XGNN3GQ  L LVW RPRDSPLS BYG 3E YIFTCVR CW CCMR4OVRCWIDMU 3E 6IU WLVQC NR3TVZA8ENTSEEU"
#cadena_cero = t
print(len(cadena_cero))    


def distancias(cadena_cero):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    cadena_cero = cadena_cero.upper()
    secuencias = cadena_cero.split() #separa por espacios en sub string 
    print("secuences: ",secuencias)
    distancias_list=[]
    for s in list(OrderedDict.fromkeys(secuencias)):
        count = secuencias.count(s)
        if count > 1:
            index = secuencias.index(s)
            lastIndex = len(secuencias) - secuencias[::-1].index(s) - 1
            distancia = 0
            for i in range(index, lastIndex):
                distancia += len(secuencias[i])
            print(s, index, lastIndex, distancia)
            distancias_list.append(distancia)
    mcd_distancias=mcd.mcd(distancias_list)        
    print ("mcd: ",mcd_distancias)
    print(" ")
    return mcd_distancias
mcd_distancias=distancias(cadena_cero)
#mcd_distancias=1
#cada letra de clave se vuelve a aplicar otra vez cuando han pasado n caracteres, la logitud sera un mcd entre las distancias encontradas.            

#usar en anaisis de patrones
def divive_bloque(string):
    strings = "".join(string.split())
    bloques = [strings[i:i+mcd_distancias] for i in range(0, len(strings), mcd_distancias)]
    bloques_por_linea = [[] for i in range(0, mcd_distancias)]
    for bloque in bloques:
        for i in range(0,len(bloque)):
            bloques_por_linea[i].append(bloque[i])
            #print (i," ",bloque[i], " ",bloques_por_linea[i])

    print(bloques)
    print(" ")
    print(bloques_por_linea)
    print(" ")
    return bloques_por_linea

#cadena_cero=divive_bloque(cadena_cero)
#group(cadena_cero)



def count(cadena_cero):
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        if (cadena_cero.count(c) >0):
            #print(c, " appears ", cadena_cero.count(c))
            return c

#count(cadena_cero)

def encrypt(cadena_cero, n):
    #print("recibo ",cadena_cero)
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([alfabeto[(alfabeto.index(c) + n + len(alfabeto)) % len(alfabeto)] if c in alfabeto else c for c in cadena_cero])
#print (encrypt(cadena_cero, -9))

def frecuencia_por_grupo(text, x):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    #text="GRCURFTNSFCVFVEQKQKPTDCPKCOWTUEKVPCUVNWQKEGRKORQGKPURQPKKGKFQTGQRPGFCRCUUCVNU"
    text = "".join([b if b in alfabeto else "" for b in text])
    clave=""
    groups = []
    for i in range(x):
        groups.append("")
    for i in range(len(text)):
        groups[i % mcd_distancias] += text[i]
    for i in range(x):
        letra_clave=count(groups[i])
        print("columna ", i," ",letra_clave," ",text.count(groups[i]))
        #text.count(groups[i])
        clave +=str(letra_clave)
        count(groups[0])
    
    print(" ")
    print(text)
    print(" ")
    print(groups)
    return clave    

clave=frecuencia_por_grupo(cadena_cero, mcd_distancias) 
VigenereAlgoritmo.decryptMensaje(clave, cadena_cero)
 