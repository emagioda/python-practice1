""""Tuplas y Desempaquetado"""


"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

lista = ["casa", "perro", "pato", "gato"]

tupla = (lista[0], lista[1], lista[2], lista[3])

assert tupla == ("casa", "perro", "pato", "gato")


"""
A partir de la siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"

lista = [tupla[0], tupla[1], tupla[2], tupla[3], tupla[4]]

assert lista == ["casa", "perro", "pato", "gato", "tenedor"]


"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])

a, b, c = tupla

assert a == "primer" and b == 25 and c == [1, 2, 3]


"""
Desempaquetar la siguiente tupla y luego sumar sus valores
"""

tupla = (87, 98, 35, 67, 4, 9)

n1, n2, n3, n4, n5, n6 = tupla
total = n1 + n2 + n3 + n4 + n5 + n6

assert total == 300


"""
Desempaquetar la siguiente lista y luego concatenar sus elementos
Restricción: Utilizar f-Strings.
"""

lista = ["esta", "mañana", "sali", "a", "correr"]

s1, s2, s3, s4, s5 = lista
string_concatenado = f"{s1} {s2} {s3} {s4} {s5}"

assert string_concatenado == "esta mañana sali a correr"


"""
Desempaquetar el primer elemento de la siguiente tupla
Restricción: Utilizar desempaquetado con comodines
"""

tupla = (73, 45, 344, 3434, 2)

primer, *_ = tupla

assert primer == 73


"""
Desempaquetar el primer y el último elemento de la siguiente lista y luego sumarlos
Restricción: Utilizar desempaquetado con comodines
"""

lista = [73, 45, 344, 3434, 2]

primero, *_ , ultimo = lista
suma = primero + ultimo

assert suma == 75


"""
Desempaquetar el primer, el segundo, el tercer, el cuarto y el quinto elemento de la
siguiente tupla y luego concatenarlos
Restricción: Utilizar desempaquetado con comodines y f-Strings
"""

tupla = ("anoche", "fui", "a", "la", "fiesta", "pero", "no", "pude", "entrar")

s1, s2, s3, s4, s5, *_ = tupla
string_concatenado = f"{s1} {s2} {s3} {s4} {s5}"

assert string_concatenado == "anoche fui a la fiesta"