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
- Fix the parser
- unit testing/turro testing
