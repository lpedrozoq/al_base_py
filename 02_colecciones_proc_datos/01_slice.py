lista_a = [1,2,3,4,5]
print(lista_a)
lista_b = lista_a
print(lista_b)
print("\n")

#Eliminación de un elemento
del lista_a[0]
print(lista_a)
print(lista_b)
print("\n")

#Id. de memoria
print(id(lista_a))
print(id(lista_b))
print("\n")

#Se hace la copia con slicing
lista_c = lista_a[:]
print(lista_c)
print(id(lista_c))
print("\n")

#Se añade un nuevo elemento
lista_a.append(6)
print(lista_a)
print(lista_b)
print(lista_c)
print("\n")

#Otra forma es hacer uso de copy:
lista_d = lista_a.copy()
print(lista_a)
print(lista_d)
print("\n")

#Se adiciona un nuevo valor
lista_a.append(7)
print(lista_a)
print(lista_d)
print("\n")















