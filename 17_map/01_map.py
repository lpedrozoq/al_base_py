print()
print(">>>Map: transformciones a una lista dado unos elementos")
print()

print("1- Haciendo una nueva lista de una forma tradicional")
numbers1 = [1,2,3,4]
numbers2 = []
for item in numbers1:
    numbers2.append(item * 2)
print(numbers1)
print(numbers2)    
print()
print()  

print("2- Haciendo una nueva lista con map")
numbers3 = list(map(lambda i : i *2, numbers1))
print(numbers3)
print()

print("3- Haciendo una nueva lista con map basado en dos listas")
numbers4 = [1,2,3,4]
numbers5 = [5,6,7]
result = list(map(lambda x,y : x + y, numbers4, numbers5))
print(result) #El lìmite serà el de la lista màs pequeña y por eso da tres items (excluye el ult. de la der.)
print()










