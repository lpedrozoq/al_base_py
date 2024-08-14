print()
print(">>>> Archivos")
print()

print("1- Leyendo archivo por linea:")
try:
    file = open("./text.txt")
    print(file.readline())
    print(file.readline())
    print(file.readline())
except FileNotFoundError as error:
  print('Error en archivo: ', error )
finally:
    print("...archivo encontrado!")  
    file.close()
print()  

