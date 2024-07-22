print()

print(">>>Funciones lambdas")
print()
add = lambda a,b :  a + b
print(add(10,4))

print()

multiply = lambda a,b : a*b
print(multiply(2,2))

#Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x : x**2, numbers))
print("Cudrados: ",squared_numbers)

print()

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)
