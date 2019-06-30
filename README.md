# TDL-1c-2019
Trabajo Practico de Teoria de Lenguajes.

## Gramatica usada

S -> D S   
D -> type N T  
N -> id  
T -> C | B  
B -> string | int | float64 | bool | []B  
C -> struct {\n L }  
L -> N T L\n | lambda  

