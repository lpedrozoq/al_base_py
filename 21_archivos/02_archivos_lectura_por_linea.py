print()
print(">>>> Archivos")
print()

print("1- Leyendo archivo completo:")
try:
    file = open("./text.txt")
    print(file.read())
except FileNotFoundError as error:
  print('Error en archivo: ', error )
finally:
    print("...archivo encontrado!")  
    file.close()
print()  

