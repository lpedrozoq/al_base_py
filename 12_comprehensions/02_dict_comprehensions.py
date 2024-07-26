print()
print(">>>Dict Comprehensions")
print()

print(">1. Creaación de diccionario tradicional")
dict ={}
for i in range(1,11):
    dict[i] = i * 2
print(dict)    
print()

print(">2. Creaación de diccionario con comprehension")
dict_v2 = { i: i * 2  for i in range(1,5)}
print(dict_v2)
print()

print(">3. Creaación de diccionario sin comprehension")
import random
countries = ['col','mex','bol','pe']
population = {}
for country in countries:
  population[country] = random.randint(1,100)
print(population)
print()  

print(">4. Creaación de diccionario con comprehension")
population_v2 = {country : random.randint(1,100)}
print(population_v2)
print()  

print(">5. Creaación de diccionario con comprehension con dos listas")
names = ["nico","zule","santi"]
ages = [12,56,98]
print(list(zip(names,ages)))
new_dict = {name : age for (name,age) in zip(names,ages)}
print(new_dict)
print()

print(">6. Otr forma de creaación de diccionario con comprehension con dos listas")
names6 = ["nico","zule","santi"]
ages6 = [12,56,98]
new_dict6 = {names6[i] : ages6[i] for i in range(len(names6))}
print(new_dict6)
print()


print(">7. Otra forma de creaación de diccionario con comprehension con dos listas")
names7 = ["nico","zule","santi"]
ages7 = [12,56,98]
#No funciona la asignación aquí:
#new_dict7 = dict(zip(names7,ages7))
#No funciona el print aquí: habrá que validar el porqué no
#print(new_dict7)
new_dict7 = {}
print(new_dict7)
print()








    