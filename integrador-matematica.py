##### A) OPERACIONES CON DNIs - -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
separador = "-"*50
#Se usa para calcular fechas y horas actuales. clase importada de datatime
#Es par calcular las edades de los DNIs
from datetime import datetime 
#importa una función para calcular los productos cartesianos entre conjuntos, listas y demás
from itertools import product


## 1    Ingreso de los DNIs (reales o ficticios).
dnis = [
    "77455677", #CONJUNTO A
    "40666027" # CONJUNTO B
]


## 2        Generación automática de los conjuntos de dígitos únicos.
conjunto_digitos = [set(dni) for dni in dnis]
def conj_digitos():
    print("CONJUNTO DE DÍGITOS ÚNICOS:\n")
    for i, conjunto in enumerate(conjunto_digitos): #se usa para iterar sobre los conjuntos de dígitos únicos
        print(f"- DNI {i+1}:{conjunto}") # imprime el conjunto de dígitos únicos


## 3        Cálculo y visualización de:
##          unión, intersección, diferencia y diferencia simétrica
union = set.union(*conjunto_digitos) #se usa para calcular la unión de los conjuntos de dígitos únicos
interseccion = set.intersection(*conjunto_digitos) #se usa para calcular la interseccion de dos conjuntos
diferencia = conjunto_digitos[0] - conjunto_digitos[1]  
diferencia_simetrica = set.symmetric_difference(conjunto_digitos[0],conjunto_digitos[1])


## 4           Frecuencia de digitos
def frecuencia_digitos():
    for i, dni in enumerate(dnis):
        frecuencia = {}
        for d in dni:
            frecuencia[d] = frecuencia.get(d, 0) + 1
        print(f"- DNI {i+1} ({dni}) :{frecuencia}")


##  5       Suma total de los dígitos de cada DNI.
def suma_digitos():
    for i, dni in enumerate(dnis):
        suma = sum(int(d) for d in dni)
        print(f"- DNI {i+1}: {suma}")


## 6 Evaluacion de condiciones lógicas






# B) Operaciones con años de nacimiento -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   


anios = [1998,1984]


# Funcion para determinar cuantos años son impares y cuantos pares.
impares = 0
pares = 0

def par_imp():
    for anio in anios: 
        if anio % 2 == 0 :
            pares +=1
        else :
            impares +=1


#Funcion para saber si un año es bisiesto
def es_bisiesto(anio):
    return(anio%4 == 0 and anio%100 != 0) or (anio%400 == 0)

def print_bi():
    if any(es_bisiesto(anio) for anio in anios):
        print("Tenemos un año especial")
    else:
        print("no tenemos ningún año bisiesto")


#  Funcion para los que nacieron después del 2000, mostrar "Grupo Z".
if all(anio > 2000 for anio in anios):
    print("GRUPO Z")












print(separador)

print("------------- OPERACIONES CON DNIs ---------------")
print(separador)
conj_digitos()
print(separador)

print("OPERACIONES CON CONJUNTOS :\n")

print(f"Unión : {union}")
print(f"Intersección : {interseccion}")
print(f"Diferencia : {diferencia}")
print(f"Diferencia simétrica : {diferencia_simetrica}")

print(separador)

print("FRECUENCIA DE DÍGITOS:\n")
frecuencia_digitos()

print(separador)

print("SUMA TOTAL DE LOS DIGITOS DE CADA DNI:\n")
suma_digitos()

print(separador)
print("-----Operaciones con años de nacimiento-----")
print(separador)

print_bi()

print(separador)
