print()
print(">>>> Archivos")
print()

print("1- Escribiendo en un archivo con w+:")
#Sobreescribe lo que hay
with open("./write.txt",'w+') as file:  
  for line in file:
      print(line)
  file.write("1-Nuevas lìneas\n")    
  file.write("2-Otras nuevas lìneas\n")
print()  

    