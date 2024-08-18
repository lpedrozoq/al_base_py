print()
print(">>>> Archivos")
print()

print("1- Escribiendo en un archivo:")
#r+: permiso de lecturas y demas cômo escritura
with open("./write.txt",'r+') as file:  
  file.write("Nuevas lìneas\n")    
  file.write("Otras nuevas lìneas\n")
  for line in file:
    print(line)
print()  

    