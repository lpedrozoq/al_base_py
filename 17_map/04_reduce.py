import functools

print()
print(">>>Reduce")
print()

print("1- Uso básico de 'reduce'en lambda en una lista de: 1,2,3,4")
numbers1 = [1,2,3,4]
result1 = functools.reduce(lambda counter, item : counter + item, numbers1)
print(result1)
print()

def accum(counter, item):
    print("Counter: ", counter)
    print("Item   : ",item)
    return counter + item
print("2- Uso de 'reduce' en función en una lista de: 1,2,3,4")
result2 = functools.reduce(accum,numbers1)
print(result2)


