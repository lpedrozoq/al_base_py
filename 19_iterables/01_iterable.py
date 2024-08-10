print()
print(">>>Iterables")
print()

print("1- Impresiòn de un rangeo normal: range(1,10)")
for item in range(1,10):
    print(item)
print()

#Aquì no es iteración todavía
print("2- Aquì no es iteración todavía")
my_iter = range(1,10)
print(my_iter)    
print()


#Aquì si es iteración
print("3- Aquì si es iteración")
my_iter = iter(range(1,10))
print(my_iter)    
print()

#Aquì imprimo de manera manual la iteración
print("4- Impresiòn manual")
print(next(my_iter))
print(next(my_iter))





    
 