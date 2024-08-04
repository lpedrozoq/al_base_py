print()
print(">>> Map")
print()

print("1-Map sin funcion lambda")
def cuadrado(numero):
    return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)
lista_resultados = list(resultado)
print(lista_resultados)
print()

print("2-Map con funcion lambda")
lista2 = [1,2,3,4,5,6,7]
resultado2 = map(lambda numero : numero * numero, lista2)
lista_resultados2 = list(resultado2)
print(lista_resultados2)
print()

#Pares
print("3-Pares")
numbers = range(11)
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)
print()