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

print(separador)
print("-----EVALUACIÓN DE CONDICIONES LÓGICAS-----")
print(separador)

#---------------------------------------------------------------------------------

# El condicional se encarga de ver si todos los conjuntos tiene al menos 5 digitos unicos.
if all(len(conjunto) >= 5 for conjunto in conjunto_digitos):
# En caso de que se cumpla la condicion, este mismo imprime alta diversidad numerica.
    print("Alta diversidad numérica.")
# En caso de que no se cumpla la condicion imprime no hay diversidad numerica
else:                                  
    print("No hay diversidad numérica suficiente.")

#---------------------------------------------------------------------------------
                                           
 # El set.intersection se implementa para buscar los digitos que estan presentes en los DNI que se usaron
digitos_comunes = set.intersection(*conjunto_digitos) 
# Si los resultados no se encuentran vacios el condicional muestra los digitos comunes.                                            
if digitos_comunes:                                   
    print(f"Dígitos comunes en todos los conjuntos: {digitos_comunes}")
# En caso contrario muestra que no hay digitos comunes.
else:
    print("No hay dígitos comunes en todos los conjuntos.")

#---------------------------------------------------------------------------------

# Aqui se utiliza la interseccion utilizada anteriormente.
if len(interseccion) == 1:
# Si solo hay un digito comun entre los conjuntos se lo considera "Representativo del grupo"
    print(f"Dígito representativo del grupo: {list(interseccion)[0]}")
# Si hay mas de uno o directamente no hay ninguno se muestra "No hay un unico  digito representativo"
else:
    print("No hay un único dígito representativo.")

#---------------------------------------------------------------------------------

# En esta porcion de codigo se cuenta cuantos conjuntos tienen una cantidad par de elementos.
pares = sum(1 for conj in conjunto_digitos if len(conj) % 2 == 0)
# Tambien se compara con los que tienen cantidad impar
impares = len(conjunto_digitos) - pares
# En caso de que haya mas pares se muestra por pantalla "Grupo par"
if pares > impares:
    print("Grupo par")
# En caso contrario se mostrara "Grupo impar o balanceado"
else:
    print("Grupo impar o balanceado")

#---------------------------------------------------------------------------------
# El siguiente condicional verifica si ningun conjunto contiene el digito "0"
if all("0" not in conj for conj in conjunto_digitos):
# En caso de que ninguno lo tenga muestra "Grupo sin ceros"
    print("Grupo sin ceros")
# Caso contrario muestra lo que contiene el print de abajo.
else:
    print("Al menos un conjunto contiene el dígito 0")
dnis = ["77455677", "40666027"]


    

# B) Operaciones con años de nacimiento -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   


anios = [1998,1984]


# Funcion para determinar cuantos años son impares y cuantos pares.


def par_imp():
    impares = 0
    pares = 0
    for anio in anios: 
        if anio % 2 == 0 : #si el año al dividirlo por dos, da resto 0, es par
            pares += 1
        else : # como no da cero, lo toma como año impar
            impares +=1
    print(f"El total de años pares es: {pares}\n El total de años impares es: {impares}")


#Funcion para saber si un año es bisiesto
def es_bisiesto(anio):
    return(anio%4 == 0 and anio%100 != 0) or (anio%400 == 0)

def print_bi():
    if any(es_bisiesto(anio) for anio in anios): # si alguno de los dos años es biciesto, se imprime:
        print("Tenemos un año especial")
    else: # si ninguno es biciesto, imprime:
        print("no tenemos ningún año bisiesto")


#  Funcion para los que nacieron después del 2000, mostrar "Grupo Z".
def grupoZ():
    if anios[0] > 2000 and anios[1] > 2000: # si ambos años son mayores a 2000, imprime:
       print("Grupo Z")
    else: # si no se cumple la condicion de arriba, imprime:
        print("Hay aunque sea un año que no es GRUPO Z")

# producto cartesiano entre el conjunto de años y el conjunto de edades actuales.

from datetime import datetime # importa una clase de un módulo de python
anio_actual = datetime.now().year #pedimos el año actual


def edades_():
    edades = []
    for anio in anios: #recorre los años
        edad = anio_actual - anio # calcula la edad
        edades.append(edad) # lo agrega a edades
    return edades

edades = edades_()
producto_cartesiano = []

def productos_cart():

    for anio in anios: # recorre los años
        for edad in edades: #recorre las edades
            producto_cartesiano.append((anio,edad)) # agrega a la lista de los productos: (anio, edad)

    for num in producto_cartesiano:
        print(num)







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

print("--------OPERACIONES CON AÑOS DE NACIMIENTO--------")
print(separador)


print("EJERCICIO -CUANTOS AÑOS NACIERON EN PARES Y CUANTOS EN IMPARES\n")
par_imp()
print(separador)
print("EJERCICIO -HAY ALGUN AÑO BISISETO?-\n")
print_bi()
print(separador)
print("EJECICIO -GRUPO Z-\n")
grupoZ()
print(separador)
print("EJERCICIO -PRODUCTOS CARTESIANOS-\n")
productos_cart()

print(separador)
