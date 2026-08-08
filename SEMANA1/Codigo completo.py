'''
CODIGO COMPLETO

'''

n=int(input("Por favor ingresar un numero: "))

def pnc():
    

    if n == 0:
        print("El numero ingresado es cero")
    elif n>0:
        print("El numero ingresado es positivo")
    elif n<0:
        print("El numero ingresado es negativo") 


def par_impar():

    if n % 2 == 1:
        print("El numero", n, "es impar")
    elif n % 2 == 0:
        print("El numero", n, "es par")


def fibonacci():

    a=0
    b=1

    while a < n:

        a, b = b, b + a

    if a == n:
        print("El numero es parte de la secuencia de Fibonacci")
    elif a != n:
        print("El numero no es parte de la secuencia de Fibonacci")


def suma_intermedios():

    a=int(input("Por favor ingresar el primer limite: "))
    b=int(input("Por favor ingresar el segundo limite: "))

    sum_tot=0

    while a<=b:
        sum_tot = sum_tot + a
        a = a + 1


    print("La suma de los numeros intermedios mas sus limites es:", sum_tot)

def vocales_consonantes():

    mes = input("Ingrese un mes: ")

    for letra in mes:
        if letra in "aeiou":
            print(letra, "es vocal")
        else:
            print(letra, "es consonante")

def posicion_letra():

    letra = input("Ingrese una letra: ")

    abecedario = "abcdefghijklmnopqrstuvwxyz"

    posicion = abecedario.find(letra) + 1

    print("La letra", letra, "esta en la posicion", posicion)


pnc()
par_impar()
fibonacci()
suma_intermedios()
vocales_consonantes()
posicion_letra()
