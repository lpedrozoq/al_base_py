print()
print(">>>Modificaciòn de conjuntos")
print()

print("> set_countries {'col','mex','bol'}")
set_countries = {'col','mex','bol'}
size = len(set_countries)
print(set_countries)
print("Tamaño: ", size)
print()

print(">Buscar elemento en cojunto:")
print("'col' in set_countries : ", "col" in set_countries)
print("'ven' in set_countries : ", "ven" in set_countries)
print()

print(">Adicionar elemento a conjunto")
set_countries.add("pe")
print(set_countries)
print()

print(">Actuzlizar elemento a conjunto")
set_countries.update({'ar','ec','pe'})
print(set_countries)
print()

print(">Remover elemento a conjunto")
set_countries.remove('ar')
print(set_countries)
print()

print(">Remover elemento de un conjunto")
try:
    set_countries.remove('arg')
    print(set_countries)
    print()
except Exception as exc:
    print(exc)
finally:
    print("Error. 'arg' no existe!")    
    print()

print(">Remover elemento de un conjunto (sin necesidad de try/except)")
set_countries.discard('arg')
print(set_countries)
print()

print(">Limpiar elemento de un conjunto")
set_countries.clear()
print(set_countries)
print()

print(">Tamaño del conjunto")
set_countries.add("co")
print(set_countries)
print(len(set_countries))
print()


    
    








