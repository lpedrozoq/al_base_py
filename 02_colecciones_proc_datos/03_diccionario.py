numbers = {1:"uno",2:"dos",3:"tres"}
print("\n")
print(numbers)
print(numbers[2])
print("\n")


#Otro ejemplo
information = {"nombre":"Leo","apellido":"Pedrozo","edad":45,"fecha_nacimiento": "1979-01-16"}
print(information)
print(information["nombre"])

#Borrado de un elemento del diccionario
del information["apellido"]
print(information)
print("\n")

#Info extra de los diccionarios
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
print(type(values))
pairs = information.items()
print(pairs)

