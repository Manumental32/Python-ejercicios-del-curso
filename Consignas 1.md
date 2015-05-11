Ejercicio N° 1
-	Definir una función que devuelva True o False dependiendo si una lista, string o tupla es o no capicúa.
-	Lo ideal es hacerla genérica y que funcione con cualquier tipo de dato.
-	Lo más sencillo es hacerlo solo para listas…
-	Intenten no googlear la solución (algunas son horribles, pero están).
-	El pensamiento lateral ayuda, y mucho.

def capicua(L):
                “determina si una lista, string o tupla es o no capicua”
                …
                …
                return …

El uso sería el siguiente:
>>> capicua("abc")        # strings
False
>>> capicua("aba")
True
>>> capicua([1,2,3])      # listas
False
>>> capicua([1,2,1])
True
>>> capicua((1,2,3))      # tuplas
False
>>> capicua((1,2,1))
True


Ejercicio N° 2
-	Definir una función que clasifique un triángulo según sus lados.
-	Versión sencilla: equilátero, isósceles o escaleno.
-	Versión sofisticada: además de lo anterior, rectángulo, acutángulo u obtusángulo.

def triangulo(a, b, c):
                “clasifica un triángulo según sus lados”
                …
                …
                return …

El uso sería el siguiente:
>>> triangulo(3,3,3)
'equilatero'
>>> triangulo(1,2,3)
'escaleno'
>>> triangulo(4,5,5)
'isosceles'
>>> triangulo(4,4,6)
'isosceles'
>>> triangulo(3,4,3)
'isosceles'


Ejercicio N° 4
-	Definir una función que imprima los n próximos años bisiestos a partir de un año determinado.
-	Usar la función definida en el ejercicio anterior.

def listar(aa, n):
                “imprime años bisiestos”
                …
                …

El uso sería el siguiente:
>>> listar(1994, 3)
1996
2000
2004
>>> listar(2092, 4)
2092
2096
2104
2108



Ejercicio N° 5
-	Escribir una función que devuelva una lista con números que son divisibles por 7 pero no por 5, en un rango a (inclusive), b(exclusive).
-	Considerar el uso de la función range(inicio, fin) para generar una secuencia de números.
-	Considerar el uso de la función append para agregar elementos al final de una lista.

def div7no5(a, b):
                “devuelve los divisibles por 7 pero no por 5 en un rango”
                …
               return …

El uso sería el siguiente:
>>> div7no5 (7, 49)
[7, 14, 21, 28, 42]


Ejercicio N° 6
-	Escribir una función que devuelva el factorial de n.

def fact(n):
                “devuelve el factorial de n”
                …
               return …

El uso sería el siguiente:
>>> fact (7)
5040
