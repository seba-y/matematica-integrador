# A) OPERACIONES CON DNIs - -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
separador = "-"*50
#Se usa para calcular fechas y horas actuales. clase importada de datatime
#Es par calcular las edades de los DNIs
from datetime import datetime 
#importa una función para calcular los productos cartesianos entre conjuntos, listas y demás
from itertools import product


# 1) INGRESO DE LOS DNIs (REALES O FICTICIOS).

dnis = [
    "77455677", #CONJUNTO A
    "40666027" # CONJUNTO B
]


# 2) GENERACION AUTOMATICA DE LOS CONJUNTOS DE DIGITOS UNICOS.

conjunto_digitos = [set(dni) for dni in dnis]
def conj_digitos():
    print("CONJUNTO DE DÍGITOS ÚNICOS:\n")
    for i, conjunto in enumerate(conjunto_digitos): #se usa para iterar sobre los conjuntos de dígitos únicos
        print(f"- DNI {i+1}:{conjunto}") # imprime el conjunto de dígitos únicos


# 3) CALCULO Y VISUALIZACION DE:
#          unión, intersección, diferencia y diferencia simétrica
union = set.union(*conjunto_digitos) #se usa para calcular la unión de los conjuntos de dígitos únicos
interseccion = set.intersection(*conjunto_digitos) #se usa para calcular la interseccion de dos conjuntos
diferencia = conjunto_digitos[0] - conjunto_digitos[1]  
diferencia_simetrica = set.symmetric_difference(conjunto_digitos[0],conjunto_digitos[1])


# 4) FRECUENCIA DE DIGITOS.

def frecuencia_digitos():
    for i, dni in enumerate(dnis):
        frecuencia = {}
        for d in dni:
            frecuencia[d] = frecuencia.get(d, 0) + 1
        print(f"- DNI {i+1} ({dni}) :{frecuencia}")


# 5) SUMA TOTAL DE LOS DIGITOS DE CADA DNI.

def suma_digitos():
    for i, dni in enumerate(dnis):
        suma = sum(int(d) for d in dni)
        print(f"- DNI {i+1}: {suma}")


# 6) EVALUACION DE CONDICIONES LOGICAS.

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

#---------------------------------------------------------------------------------

# B) OPERACIONES CON A Operaciones con años de nacimiento.   

# Se crea una lista con los años de nacimiento de cada individuo.
años = [1998, 1984]

#---------------------------------------------------------------------------------

# Funcion para determinar cuantos años son pares y cuantos impares.
def contar_pares_impares(lista_años):
    # Inicio de contadores para los años pares e impares.
    pares = 0
    impares = 0
    for año in lista_años: 
        if año % 2 == 0 :
            pares +=1
        else :
            impares +=1

#---------------------------------------------------------------------------------

# Esta funcion corrobora si el año es bisiesto.
def es_bisiesto(año):
    return(año%4 == 0 and año%100 != 0) or (año%400 == 0)

#---------------------------------------------------------------------------------

# Funcion que verifica si hay por lo menos un año bisiesto en la lista de años e imprime un mensaje segun que.
def verificar_años_bisiestos(lista_años):
    if any(es_bisiesto(año) for año in lista_años):
        print("Tenemos un año especial")
    else:
        print("no tenemos ningún año bisiesto")

#---------------------------------------------------------------------------------

# Este condicional verifica si todos los años en la lista son mayores a los 2000, se identifica como "Grupo Z"
def verificar_grupo_z(lista_años):
    if all(año > 2000 for año in lista_años):
        print("GRUPO Z")

#---------------------------------------------------------------------------------

verificar_años_bisiestos(años)
verificar_grupo_z(años)


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

print(f"Años pares: {pares}, Años impares: {impares}")

print(separador)