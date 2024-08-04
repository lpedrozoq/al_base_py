print()
print(">>>Funciones lambdas")
print()

print("1- add = lambda a,b :  a + b:")
add = lambda a,b :  a + b
print(add(10,4))
print()

print("2- multiply = lambda a,b : a*b")
multiply = lambda a,b : a*b
print(multiply(2,2))
print()

#Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x : x**2, numbers))
print("3- Lista para armar el cuadrado por cada nùmero")
print("Cudrados: ",squared_numbers)
print()

print("4- Lista para armar el cuadrado por cada nùmero y filtrar sòlo los pares")
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)
print()

print("5- lambda con una variable de texto para concatenar")
full_name = lambda name, last_name :f"Full name is {name.title()} {last_name.title()}"
print(full_name('Leonel','Pedrozo'))
print()

print("6- Llamar directamente la lambda")
print((lambda x : x * 2)(6))
print()
