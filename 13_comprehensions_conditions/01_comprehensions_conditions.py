import random

print()
print(">>>>Comprehensions conditions")
print()


print("1-Comprehensions conditions normal (sin condicion)")
countries_1 = ['col','mex','bol','pe']
population_1 = {country : random.randint(1,100) for country in countries_1}
print(population_1)
print()

print("2-Comprehensions conditions normal (con condicion)")
result_2 = {country : population for(country,population) in 
    population_1.items() if (population > 20) }
print(result_2)
print()

print("3-Comprehensions conditions normal (con condicion para vocales)")
text = "Hola, soy Nicolas"
print("Texto a imprimir: ", text)
unique = {c : c.upper() for c in text if c in 'aeiou'}
print(unique)
print() 

print("4-Comprehensions conditions normal (con condicion para vocales y la cantidad)")
text = "Hola, soy Nicolas"
print("Texto a imprimir: ", text)
unique = {c : text.count(c) for c in text if c in 'aeiou'}
print(unique)
print() 










