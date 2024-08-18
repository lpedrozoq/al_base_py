print()
print(">>>Funciones: multiples variables ")
print()

print("1- Un sólo parámetro: def sumav1(num)")
def sumav1(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
print(sumav1([1,3,5,14]))
print()

print("2- Múltiples variables: def sumav2(*num)")
def sumav2(*numeros):
    print("Tipo de dato: ", type(numeros))
    total = 0;
    for n in numeros:
        total += n
    return total
print(sumav2(1,3,5,14))
print()

print("3- Múltiples variables nombradas: def sumav3(**num)")
def sumav3(**numeros):
    total = 0;
    for key, value in numeros.items():
        print("Key - value: ", key,value)
        total += value
    return total
di = {'a':10,'b':20}
print(sumav3(**di))
print()


    

