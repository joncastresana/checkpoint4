# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
from decimal import Decimal
sample_list = ["item1", "item2", "item3"]
sample_tuple = ("item4", "item5", "item6")
sample_float = 0.7
sample_integer = 0
sample_decimal = Decimal(0.1223233233322)
sample_dictionary = {

    "item7_key" : ["item7_value1", "item7_value2"],
    "item8_key" : ["item8_value1", "item8_value2"],
    "item9_key" : ["item9_value1", "item9_value2"]

}

# Exercise 2: Round your float up.
import math
sample_float = (math.ceil(sample_float))

# Exercise 3: Get the square root of your float.

print(math.sqrt(sample_float))

# Exercise 4: Select the first element from your dictionary.

conversión_lista = list(sample_dictionary.items())
first_element = conversión_lista[0]
print(first_element)

# Exercise 5: Select the second element from your tuple.

second_element = sample_tuple[1]
print(second_element)

# Exercise 6: Add an element to the end of your list.

sample_list.append("new element")

# Exercise 7: Replace the first element in your list.

sample_list[0] = "replaced_element" 

# Exercise 8: Sort your list alphabetically.

sample_list.sort()

# Exercise 9: Use reassignment to add an element to your tuple.

sample_tuple += ("new element",)


''' PREGUNTAS TEÓRICAS

-¿Cuál es la diferencia entre una lista y una tupla en Python?

La principal diferencia reside en que las listas son mutables y las tuplas inmutables.
Por ejemplo a una lista se le pueden añadir/borrar elementos, cambiar el orden de estos, etc etc..mientras que las tuplas(al igual que con las strings) son inmutables. Esto es si queremos
modificar el contenido de una tupla, deberíamos reasignar su contenido.
Por lo tanto cuando queramos que el contenido no sea modificable deberiamos usar tuplas. 
Un ejemplo de buenas prácticas en las listas sería tratar de almacenar el mismo tipo de dato en estas, python nos permite almacenar cualquier tipo de dato en las listas, sin embargo si
deseamos operar con los elementos de estas listas necesitariamos que estos sean operables entre sí, de lo contrario podrían aparecer errores.

-¿Cuál es el orden de las operaciones?

1º: PARENTESIS
2º: EXPONENTES
3º: MULTIPLICACIONES
4º: DIVISIONES
5º: SUMAS
6º: RESTAS

-¿Qué es un diccionario Python?

Un diccionario en Python es similar a un diccionario real, el libro de toda la vida. 
Al igual que en los diccionarios reales, cada entrada se compone de un elemento (localizador) y un valor asociado a este.
En python el elemento localizador es llamado "key" y cada "key" puede contener multitud de datos asociados a esta.

-¿Cuál es la diferencia entre el método ordenado y la función de ordenación?

El método ordenado "sorted()" devuelve un valor ordenado(por ejemplo una lista) que podrá almacenarse en una nueva variable, sin modificar la variable orginal.
La función de ordenación "sort()" sin embargo, directamente modifica el contenido de la variable.

-¿Qué es un operador de asignación?

Un operador de asignacion es el carácter utilizado para asignar un valor a una variable. 
Por ejemplo en phyton es utlizado el carácter "=" para asignar valores a una variable ( variable = valor ) y tambien ":" para asignar valores a una llave de diccionario ( "item7_key" : ["item7_value1", "item7_value2"] )
Es posible tambien combinar operadores de asignación junto con operadores matematicos para simplificar código, por ejemplo: 
total = total + 10 
total += 10 









'''






