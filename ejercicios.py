#!/usr/bin/python

import re
"""Escribe una funcion numerosPares(numeros) que devuelva los numeros pares que hay en una lista y la suma de esos elementos"""
def numerosPares(numeros):
    lista = []
    resultado = 0
    for x in range(len(numeros)):
        if numeros[x] % 2 == 0:
            lista.append(numeros[x])
        else:
            resultado += numeros[x]

    lista.append(resultado)
    return lista

"""Escribe una funcion maximo(numeros) que devuelva el elemento mas grande de una lista"""
def maximo(numeros):
    maximo = 0
    for x in range(len(numeros)):
        if numeros[x] >= maximo:
            maximo = numeros[x]

    return maximo

"""Dada una matriz representada como una lista, escribe una funcion dims(lista) que devuelva sus dimensiones"""
def dims(lista):
    dimensiones = [len(lista), len(lista[0])]

    return dimensiones

"""Escribe una funcion combinar(la, lb) que dadas dos listas devuelva una lista conteniendo los elementos de ambas listas ordenados de forma ascendente"""
def combinar(la, lb):
    for x in range(len(la)):
        lb.append(la[x])

    lb.sort()
    return lb

"""La traspuesta de una matriz se obtiene intercambiando filas y columnas. Escribe una funcion que devuelva la traspuesta de una matriz"""
def traspuesta(matriz):
    dimensiones = dims(matriz)
    for x in range(dimensiones[0]):
        for y in range(dimensiones[1]):
            matrizTraspuesta[matriz[x]][matriz[y]]

    return matrizTraspuesta

"""Escribe una funcion factores_primos(num) que devuelva una lista con la descomposicion en factores primos de num"""
def factores_primos(num):
    dividendo = num
    divisor = 2
    factores = []

    while dividendo != 1:
        if dividendo % divisor == 0:
            factores.append(divisor)
            dividendo = dividendo / divisor
        else:
            divisor += 1

    return factores

"""Escribe una funcion sumaAcumulada(numeros) a la que se le pase una lista de numeros y devuelva una lista en la que el elemento i-esimo se obtiene como la suma de los elementos de la lista entre las posiciones 0 e i. Por ejemplo, para [1,2,3] seria [1,3,6]"""
def sumaAcumulada(numeros):
    lista = []
    resultado = 0
    for x in range(len(numeros)):
        resultado += x
        lista.append(resultado)

    return lista

"""Escribe una funcio combinarListas(l1, l2) que devuelva una lista que este formada por todos los elementos de l1 y a continuacion todos los de l2"""
def combinarListas(l1, l2):
    listaCombinada = []
    listaCombinada = l1
    for x in range(len(l2)):
        listaCombinada.append(x)

    return listaCombinada

"""Escribe una funcion eliminar(l1, l2) que dadas dos listas devuelva una lista en la que esten todos los elementos de l1 que no estan en l2"""
def eliminar(l1, l2):
    nuevaLista = []
    for x in l1:
        if x not in l2:
            nuevaLista.append(x)

    return nuevaLista

"""Escribe una funcion contarLetras(palabra) que tome una palabra como argumento y devuelve una lista de pares en la que aparece cada letra junto con el numero de veces que aparece esa letra en la palabra"""
def contarLetras(palabra):
    lista = []
    contadas = []
    for x in palabra:
        if x not in contadas:
            contadas.append(x)
            lista.append((x, palabra.count(x)))

    return lista

"""Escribe una funcion longs(cadenas) a la que le pasa una lista de cadenas y devuelve una lista con las longitudes de cada una de ellas"""
def longs(cadenas):
    lista = []
    for x in cadenas:
        lista.append(len(x))

    return lista

"""Escribe una funcion cadena_mas_larga(cadenas) a la que se pasa una lista de palabras y que devuelva la palabra mas larga"""
def cadena_mas_larga(cadenas):
    cadenaMasLarga = ""
    for x in cadenas:
        if len(x) >= len(cadenaMasLarga):
            cadenaMasLarga = x

    return cadenaMasLarga

"""Escribe una funcion cadena_mas_larga(cadenas, n) a la que se le pasa una lista de palabras y un numero y que devuelva las palabras con longitudes mayores que n"""
def cadena_mas_larga2(cadenas, n):
    cadenaLarga = ""
    listaPalabras = []
    for x in cadenas:
        if len(x) > n:
            listaPalabras.append(x)

    return listaPalabras

"""Escribe una funcion obtenerPotencias(numero) que devuelva una lista del siguiente tipo[numero^2, (numero-1)^2,...,0, 1^2, 2^2,...numero^2"""
def obtenerPotencias(numero):
    listaPotencia = []
    cont = numero
    while cont >= 0 :
        listaPotencia.append(pow(cont, 2))
        
        cont = cont - 1
    
    listaPotencia += listaPotencia[len(listaPotencia)-2::-1]

    return listaPotencia

"""Escribe una funcion sumaPrimerDigito(numeros) que devuelva la suma de los primeros digitos de todos los numeros de la lista que se pasa como argumento"""
def sumaPrimerDigito(numeros):
    resultado = 0
    for x in numeros:
        resultado += int(str(x)[0])

    return resultado

"""Escribe una funcion mayoresMedia(numeros) que devuelva una lista con los numeros que son mayores que la media"""
def mayoresMedia(numeros):
    media = 0
    listaMedia = []
    for x in numeros:
        media += x
    media = media / len(numeros)
    print(media)
    for x in numeros:
        if x > media:
            listaMedia.append(x)

    return listaMedia

"""Escribe una funcion eliminarLetras(palabra,letra) que devuelva una version de palabra que no contiene el caracter letra"""
def eliminarLetras(palabra, letra):
    nuevaPalabra = ""
    for x in palabra:
        if x != letra:
            nuevaPalabra += x

    return nuevaPalabra

"""Escribe una funcion mayusculasMinusculas(palabra) que devuelva una cadena en la que las mayusculas y las minusculas esten al contrario"""
def mayusculasMinusculas(palabra):
    nuevaPalabra = ""
    for x in palabra:
        if x == x.lower():
            nuevaPalabra += x.upper()
        else:
            nuevaPalabra += x.lower()

    return nuevaPalabra

"""Escribe una funcion buscar(palabra, sub) que devuelva la posicion en la que se puede encontrar sub dentro de palabra o -1 en caso de que no este"""
def buscar(palabra, sub):
    posicion = 0
    contadorPosicion = 0
    for x in palabra:
        if x == sub:
            posicion = contadorPosicion
        else:
            contadorPosicion += 1
    
    if posicion == 0:
        posicion == -1

    return posicion

"""Escribe una funcion numVocales(palabra) que devuelva el numero de vocales que aparece en la palabra"""
def numVocales(palabra):
    numeroVocales = 0
    vocalesContadas = []
    for x in palabra:
        if re.match("(a|e|i|o|u)", x):
            vocalesContadas.append(x)
            numeroVocales = len(vocalesContadas)

    return numeroVocales

"""Escribe una funcion vocales(palabra) que devuelva las vocales que aparecen en la palabra"""
def vocales(palabra):
    vocalesContadas = []
    for x in palabra:
        if re.match("(a|e|i|o|u)", x):
            vocalesContadas.append(x)

    return vocalesContadas

"""Escribe una funcion mayusculas(palabra) que devuelva la palabra pasada a mayusculas"""
def mayusculas(palabra):
    return palabra.upper()

"""Escribe una funcion inicioFinVocal(palabra) que determina si una palabra empieza y acaba con una vocal"""
def inicioFinVocal(palabra):
    if re.match("(a|e|i|o|u)", palabra[0].lower()) and re.match("(a|e|i|o|u)", palabra[-1].lower()):
        return True
    else :
        return False

"""Escribe una funcion eliminaVocales(palabra) que elimine todas las vocales que aparecen en la palabra"""
def eliminaVocales(palabra):
    nuevaPalabra = ""
    for x in palabra:
        if not re.match("(a|e|i|o|u)", x):
            nuevaPalabra += x

    return nuevaPalabra

"""Escribe una funcion esInversa(palabra1, palabra2) que determina si una palabra es la misma que la otra pero con los caracteres en orden inverso"""
def esInversa(palabra1, palabra2):
    if palabra1[::-1] == palabra2:
        return True
    else:
        return False

"""Escribe una funcion que devuelva la transcripcion mRNA dada una secuencia DNA"""
def transcripcion_mRNA(cadena):
    nuevaCadena = ""
    for x in cadena:
        if x == "A":
            nuevaCadena += "U"
        elif x == "T":
            nuevaCadena += "A"
        elif x == "C":
            nuevaCadena += "G"
        else:
            nuevaCadena += "C"

    return nuevaCadena

"""Escribe una funcion contarLetras(palabra) al que se le pasa una palabra y devuelve un diccionario que cuenta el numero de veces que aparece cada letra"""
def contarLetrasDiccionario(palabra):
    letras = []
    cantidad = []
    contadas = []
    for x in palabra:
        if x not in contadas:
            contadas.append(x)
            letras.append(x)
            cantidad.append(palabra.count(x))
    diccionario = dict(zip(letras, cantidad))

    return diccionario

"""Escribe una funcion invertirDiccionario(d) al que se le pasa un diccionario y devuelve un diccionario que invierte claves y valores"""
def invertirDiccionario(d):
    diccionarioInvertido = {}

    return diccionarioInvertido



if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,10]
    segundaLista = [2,5,9,11,5,8,3]
    terceraLista = [2,5,9,11,5,8,3]
    cuartaLista = [1,3,4,8,5,6,0]
    quintaLista = [12, 23, 11]
    matriz = [[1,2,2,3], [2,1,1,0]]
    listaCadenas = ["telefono", "coche", "mesa", "silla", "camiseta", "boligrafo"]
    print(numerosPares(lista))
    print(maximo(lista))
    print(dims(matriz))
    print(combinar(lista, segundaLista))
    """print(traspuesta(matriz))"""
    print(factores_primos(237))
    print(sumaAcumulada(lista))
    print(combinarListas(lista, terceraLista))
    print(eliminar(cuartaLista, terceraLista))
    print(contarLetras("telefono"))
    print(longs(listaCadenas))
    print(cadena_mas_larga(listaCadenas))
    print(cadena_mas_larga2(listaCadenas, 7))
    """print(obtenerPotencias(cuartaLista))"""
    print(sumaPrimerDigito(quintaLista))
    print(mayoresMedia(cuartaLista))
    print(eliminarLetras("telefono", "e"))
    print(mayusculasMinusculas("TeleFoNo"))
    print(buscar("telefono", "f"))
    print(numVocales("telefono"))
    print(vocales("telefono"))
    print(mayusculas("telefono"))
    print(inicioFinVocal("casa"))
    print(eliminaVocales("telefono"))
    print(esInversa("casa", "asac"))
    print(transcripcion_mRNA("ATCGATTG"))
    print(contarLetrasDiccionario("telefono"))
