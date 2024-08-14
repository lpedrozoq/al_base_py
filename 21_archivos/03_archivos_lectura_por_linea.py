print()
print(">>>> Archivos")
print()

print("1- Leyendo archivo completo:")
#De esta manera, el 'with' se encarga de cerrar el archivo
with open("./text.txt") as file:
  for line in file:
    print(line)
print()  

    