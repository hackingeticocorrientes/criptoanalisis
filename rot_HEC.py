#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Feb 19 05:59:22 2020

@author: Rafael Perez

"""
import string

def cripto(frase):

    alfabeto = string.ascii_uppercase
    print alfabeto    
    for i in range(0, 26):
        print "rot "+ str(i)
        salida = ""
        for letra in frase:
            busca = alfabeto.find(letra)+i
            modulo = busca % 26
            salida += str(alfabeto[modulo])
        print salida, "\n"

#input("\n\nPressione Enter para continuar")


frase = "abcd"
frase = frase.replace(" "," ").upper() # considerar espacio valor ascii
cripto(frase)