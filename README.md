# TDL-1c-2019
Trabajo Practico de Teoria de Lenguajes.

## Gramatica usada

S -> D S | D   
D -> type id T  
T -> C | B | id  
B -> string | int | float64 | bool | []T  
C -> struct {\n L }  
L -> id T L\n | lambda  

## TODO
- El diccionario que generamos en parser.py mantiene orden de insercion 
(solo en python 3.6+), por lo que nuestros json quedan con los atributos en el 
orden inverso que el archivo de entrada. FIXED
- Si queremos que corra en python 3.5 o menos, hay que usar orderedDict en el parser
- Detect border cases.
- Detect dependency cicles.
