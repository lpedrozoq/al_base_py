s = [1,4,9,16,25]

print("\n")
print(">>> Lista")
print(s)
print("\n")

print(s[0])
print(s[1])
print(s[-1])
print(s[-3])
print("\n")

print(">>> Copia lista")
t = s[:]
print(t)
print("\n")

#Concatenación
print(">>> Concatenación lista")
u = t + [36, 49, 64, 81, 100]
print(u)
print("\n")

#Reemplazando un valor
print(">>> Reemplazando un valor")
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)
print("\n")

#Adicionando nuevos elementos
print(">>> Adicionando nuevos elementos")
cubes.append(216)
cubes.append(7**3)
print(cubes)
print()

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
print(">>> Adicionando nuevos elementos")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(f"Longitud: {len(letters)}")
#replace some values
print("> Reemplazando valores: [2:5] =[]")
letters[2:5] =[]
print(letters)
#clear the list by replacing all the elements with an empty list
print("> Lista vacía")
letters[:] = []
print()

#nested list
print(">>> Nested list")
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print()


# Fibonacci serie:
# the sum of two elements defines the next

a,b = 0,1
print(a,b)
print(">>> Serie Fibonacci:")
while(a<10):
    print(a)
    a,b = b, a+b

