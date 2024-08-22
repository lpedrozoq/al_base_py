print()
print(">>>>Antoaciones")
print()

print(">1- Usando tipado: def circumferenceV1(radius : float)-> float:")
import math
def circumferenceV1(radius : float)-> float:
    return 2 * math.pi * radius

print(circumferenceV1.__annotations__)
print(circumferenceV1(1.23))
print()

print(">2- Usando tipado(v2): def circumferenceV2(radius : float, radius2 : float)-> float:")
import math
def circumferenceV2(radius : float, radius2 : float)-> float:
    return 2 * math.pi * radius * radius2

print(circumferenceV2.__annotations__)
print(circumferenceV2(1.23, 2.34))
print()
