#Importa un modulo para calcular raiz cuadrada
import math
math.sqrt(9)

#Importa solo la funcion para calcular la raiz
from math import sqrt
sqrt(9)

#Importar modulos con un alias
import math as m
m.sqrt(9)

#Importando solo la funcion con un alias
from math import sqrt as s
s(9)

#Built-in Modules: Muestra una lista de modulos disponibles para usar en Python
import sys
sys.builtin_module_names
help('modules')

#Mostrando informacion de el modulo math
import math
help(math)
