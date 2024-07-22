"""
*Se pueden modificar
*No tienen un orden
*No permite duplicados
"""
print()
print(">>>Conjuntos (como set en 'java')")
set_countries = {'col','mex','col'}
print(set_countries)
print(type(set_countries))
print()

print("> Crecion a partir de otro elemento: string")
set_from_string = set('hola')
print(set_from_string)

print()

print("> Creacion a partir de otro elemento: tupla")
set_from_tupla = set(('hola','a','todos','hola'))
print(set_from_tupla)

print()

numbers = [1,2,3,4,5,6,5,2]
set_numbers = set(numbers)
print("> Creacion a partir de otro elemento: lista de nùmeros (y se pasan luego a una lista)")
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)

print()




