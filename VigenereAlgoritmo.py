#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Fri 12 20:18:40 2019

@author: Rafael Ernesto Perez

"""
import pyperclip

#simbolos del alfabeto
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():

    cadena = "Salve insigne y altiva Corrientes, Legendaria de invicto broquel, Colosal y gentil amazona Que en tu frente se ostenta un laurel! ¡Empujabas a tus hijos valientes A salvar a la Patria o morir, tu sien arrogante la gloria Del laurel iba siempre a ceñir!" # himno de corrientes primer parrafo
    clave = 'VERA'
    modo = 'encrypt' # me permite usar menos parametros

    if modo == 'encrypt':
        traduccion = encryptMensaje(clave, cadena)
    elif modo == 'decrypt':
        traduccion = decryptMensaje(clave, cadena)

    print('%sed message:' % (modo.title()))
    print(traduccion)
    pyperclip.copy(traduccion)
    print()
    print('The message has been copied to the clipboard.')


def encryptMensaje(clave, message):
    return translateMensaje(clave, message, 'encrypt')


def decryptMensaje(clave, message):
    return translateMensaje(clave, message, 'decrypt')


def translateMensaje(clave, message, mode):
    traduccion = [] # contiene cadena encriptada o desencriptada
    claveIndex = 0
    clave = clave.upper()

    for simbolo in message: 
        num = letras.find(simbolo.upper())
        if num != -1: # pasao todo a maysusculas para ser mas practico
            if mode == 'encrypt':
                num += letras.find(clave[claveIndex]) 
            elif mode == 'decrypt':
                num -= letras.find(clave[claveIndex]) 

            num %= len(letras) # deriva de la formula que genera la tabla 

            # dada la tablaa
            if simbolo.isupper():#defino movimiento en colunas
                traduccion.append(letras[num])
            elif simbolo.islower():
                traduccion.append(letras[num].lower())

            claveIndex += 1 
            if claveIndex == len(clave):
                claveIndex = 0
        else:
            # por si no aparece el simbolo
            traduccion.append(simbolo)

    #print (''.join(traduccion))
    return ''.join(traduccion)



if __name__ == '__main__':
    main()