print()
print(">>>Comprehensions, funciones y manejo de errores")
print()

numbers = []
print(">1. Iteración normal")
for element in range(1,15):
  numbers.append(element)     
print(numbers)
print()

print(">2. Iteración en una sóla línea de código")
numbers_v2 = [element for element in range(16,20)]
print(numbers_v2)
print()

print(">3. Iteración en una sóla línea de código con expresión")
numbers_v3 = [element * 3 for element in range(16,20)]
print(numbers_v3)
print()

print(">4. Iteración normal con condicional")
for element in range(1,15):
    if element  % 2 == 0:       
        numbers_v3.append(element)     
print(numbers_v3)
print()

print(">5. Iteración en una sóla línea de código y con condicionl")
numbers_v4 = [element * 2 for element in range(16,20) if element % 2 == 0]
print(numbers_v4)
print()



