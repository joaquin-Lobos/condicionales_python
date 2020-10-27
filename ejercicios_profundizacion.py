#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    numero_1 = float(input('Ingrese el primer número:\n'))
    numero_2 = float(input('Ingrese el segundo número:\n'))

    resultado_resta = numero_1 - numero_2

    if resultado_resta > 0:
        print("El resultado es positivo")
    elif resultado_resta < 0:
        print("El resultado es negativo")
    else:
        print("El resultado es igual a 0")
    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''


def ej2():
    print('Ejercicios de práctica con números')

    numero_1 = int(input('Ingrese el primer número entero:\n'))
    numero_2 = int(input('Ingrese el segundo número entero:\n'))
    numero_3 = int(input('Ingrese el segundo número entero:\n'))

    if (numero_1 % 2) == 0:
        print("{} es par" .format(numero_1))
    else:
        print("{} es impar" .format(numero_1))

    if (numero_2 % 2) == 0:
        print("{} es par" .format(numero_2))
    else:
        print("{} es impar" .format(numero_2))

    if (numero_3 % 2) == 0:
        print("{} es par" .format(numero_3))
    else:
        print("{} es impar" .format(numero_3))
    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''


def ej3():
    print('Ejercicios de práctica con números')

    numero_1 = float(input('Ingrese el primer número:\n'))
    operador = str(input('Ingrese el operador de la cuenta:\n'))
    numero_2 = float(input('Ingrese el segundo número:\n'))
    
    resultado = 0

    if operador == "+":
        resultado = numero_1 + numero_2
    elif operador == "-":
        resultado = numero_1 - numero_2
    elif operador == "*":
        resultado = numero_1 * numero_2
    elif operador == "/":
        resultado = numero_1 / numero_2
    elif operador == "**":
        resultado = numero_1 ** numero_2
    else:
        print ("El operador indicado no está disponible")

    if resultado != 0:
        print("{} {} {} = {}" .format(numero_1, operador, numero_2, resultado))
    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''


def ej4():
    print('Ejercicios de práctica con cadenas')
    texto_1 = str(input('Ingrese la primera palabra:\n'))
    texto_2 = str(input('Ingrese la segunda palabra:\n'))
    texto_3 = str(input('Ingrese la tercera palabra:\n'))
    numero_1 = int(input('Ingrese el numero:\n'))

    if numero_1 == 1:
        contenedor = [texto_1, texto_2, texto_3]
        orden_alfabetico = sorted(contenedor)
        print("el orden de las palabras según orden alfabetico es:", orden_alfabetico[0], orden_alfabetico[1], orden_alfabetico[2])   
    else:
        if len(texto_1) > len(texto_2) and len(texto_1) > len(texto_3):
            c = texto_1
            if len(texto_2) > len(texto_3):
                b = texto_2
                a = texto_3
            else:
                a = texto_2
                b = texto_3
        elif len(texto_1) < len(texto_2) and len(texto_1) < len(texto_3):
            a = texto_1
            if len(texto_2) > len(texto_3):
                c = texto_2
                b = texto_3
            else:
                b = texto_2
                c = texto_3
        else:
            b = texto_1
            if len(texto_2) > len(texto_3):
                c = texto_2
                a = texto_3
            else:
                a = texto_2
                c = texto_3

    print(" el orden de las palabras segun la cantidad de caracteres es: {} {} {}" .format(a, b, c))
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''


def ej5():
    print('Ejercicios de práctica con números')

    temperatura_1 = int(input('Ingrese la primera temperatura:\n'))
    temperatura_2 = int(input('Ingrese la segunda temperatura:\n'))
    temperatura_3 = int(input('Ingrese la tercera temperatura:\n'))

    temperatura_minima = min(temperatura_1, temperatura_2, temperatura_3)
    temperatura_maxima = max(temperatura_1, temperatura_2, temperatura_3)
    promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3

    print("La temperatura minima ingresada es:", temperatura_minima)
    print("La temperatura maxima ingresada es:", temperatura_maxima)
    print("El promedio de las temperaturas ingresadas es:", promedio)
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
