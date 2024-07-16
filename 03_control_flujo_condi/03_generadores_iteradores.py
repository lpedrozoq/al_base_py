print()
print(">>>Iterador")
my_list = [1,2,3,4]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print()
text = "Hola mundo"
iter_text = iter(text)
for char in iter_text:
    print(char)

print()
limit = 10
#Creo un rango y que este tenga sólo contenga items pares
odd_iter = iter(range(0,limit + 1, 2))
for num in odd_iter:
    print(num)

print()

#Generador
print(">>>1. Generador")
def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)  
print()

print(">>>2. Generador")
def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b

for num in fibonacci(10):
    print(num)
print()


