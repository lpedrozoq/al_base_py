print()
print(">>>Modificaciòn de conjuntos")
print()

print(">1. set_countries {'col','mex','bol'}")
set_countries = {'col','mex','bol'}
size = len(set_countries)
print(set_countries)
print("Tamaño: ", size)
print()

print(">2. Buscar elemento en cojunto:")
print("'col' in set_countries : ", "col" in set_countries)
print("'ven' in set_countries : ", "ven" in set_countries)
print()

print(">3. Adicionar elemento a conjunto")
set_countries.add("pe")
print(set_countries)
print()

print(">4. Actuzlizar elemento a conjunto")
set_countries.update({'ar','ec','pe'})
print(set_countries)
print()

print(">5. Remover elemento a conjunto")
set_countries.remove('ar')
print(set_countries)
print()

print(">6. Remover elemento de un conjunto")
try:
    set_countries.remove('arg')
    print(set_countries)
    print()
except Exception as exc:
    print(exc)
finally:
    print("Error. 'arg' no existe!")    
    print()

print(">7. Remover elemento de un conjunto (sin necesidad de try/except)")
set_countries.discard('arg')
print(set_countries)
print()

print(">8. Limpiar elemento de un conjunto")
set_countries.clear()
print(set_countries)
print()

print(">9. Tamaño del conjunto")
set_countries.add("co")
print(set_countries)
print(len(set_countries))
print()

print(">10.1. Union de conjuntos (set)")
set_a = {'col','mex','bol'}
set_b = {'pe','bol'}
set_c = set_a.union(set_b)
print(set_c)
print()


print(">10.2. Union de conjuntos (set)")
set_a1 = {'col','mex','bol'}
set_b1 = {'pe','bol'}
set_c1 = set_a1 | set_b1
print(set_c1)
print()

print(">10.3. Union de conjuntos (set)")
set_a2 = {'col','mex','bol'}
set_b2 = {'pe','bol'}
print(set_a2 | set_b2)
print()

print(">11.1 intersecciòn de conjuntos (set)")
set_inter_a1 = {'col','mex','bol'}
set_inter_b1 = {'pe','bol'}
set_inter_c1 = set_inter_a1.intersection(set_inter_b1)
print(set_inter_c1)
print()


print(">11.2 intersecciòn de conjuntos (set)")
set_inter_a2 = {'col','mex','bol'}
set_inter_b2 = {'pe','bol'}
print(set_inter_a2 & set_inter_b2)
print()


print(">12.1 diferencias de conjuntos (set)")
set_dif_a1 = {'col','mex','bol'}
set_dif_b1 = {'pe','bol'}
print(set_dif_a1 - set_dif_b1)
print()
    
print(">12.2 diferencias de conjuntos (set)")
set_dif_a2 = {'col','mex','bol'}
set_dif_b2 = {'pe','bol'}
set_dif_c2 = set_dif_a2.difference(set_dif_b2)
print(set_dif_c2)
print()
    

print(">13.1 diferencias simètrica (set)")
set_dif_sim_a1 = {'col','mex','bol'}
set_dif_sim_b1 = {'pe','bol'}
set_dif_sim_c1 = set_dif_sim_a1.symmetric_difference(set_dif_sim_b1)
print(set_dif_sim_c1)
print()







