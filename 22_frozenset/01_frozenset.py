print()
print(">>>>Frozenset: set inmutables")
print()

print("1- Creando")
fs = frozenset([1,2,3])
print(fs)
print("Tipo fs: ", type(fs))
print()

print("2- Intentando agregar un elemento(controlado con try)")
try:
  fs.add(4)
except Exception as error:
  print('No es posible agregar: ', error)
finally:
  print()

