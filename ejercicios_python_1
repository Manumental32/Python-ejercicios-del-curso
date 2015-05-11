#ej1
def capicua(x):
	"determina si una lista, string o tupla es o no capicua"
	return x == x[::-1]

# print capicua((1,2,3))    

#ej2
def triangulo(x):
	"trinangulo segun sus lados"
	aux = 0
	if len(x) != 3:
		return "no es un triangulo"
	else:
		for e in x:
			if x.count(e) > aux :
				aux = x.count(e)
	t = {1:"escaleno", 2 : "isosceles", 3 : "equilatero"}
	return t[aux]

# print triangulo((3,3,3))    

#ej3
def bisiesto(anio):
	"determina si un anio es bisiesto"

	import datetime
	from datetime import timedelta

	d = datetime.date(anio,3,1)
	d = d - timedelta(days=1)

	if 29 == d.day :
		return "bisiesto"
	else:
		return "no bisiesto"

# print bisiesto(2012)

#ej4
def listar(aa,n):
	"imprime n anios bisiestos"

	import datetime
	from datetime import timedelta

	r = []
	while len(r) != n:
		if bisiesto(aa) == "bisiesto":
			r.append(aa)
			print aa
			aa += 4
		else:
			aa += 1

	return r

# listar(2092,4)


#ej5
def div7no5(a,b):
	"devuelve los divisibles por 7 pero no por 5 en un rango"

	r = []
	for n in range(a,b):
		if (n % 7 == 0) & (n % 5 != 0):
			r.append(n)
	return r

# print div7no5 (7, 49)


#ej6
def fact(n):
	"devuelve el factorial de n"
	if n > 0:
		f = n * fact(n-1)
	else:
		f = 1
	return f

print fact (7)


