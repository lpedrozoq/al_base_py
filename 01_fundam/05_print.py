print("\n>>>Usando comas para varios valores (genera un espacio): 'Nunca','pares','de','aprender'")
print("Nunca","pares","de","aprender\n")

print(">>>Usando + para varios valores (concatena): 'Nunca' + 'pares' + 'de' + 'aprender'")
print("Nunca" + "pares" + "de" + "aprender\n")

print(">>>Uso de 'sep': 'Nunca', 'pares', 'de' , 'aprender', sep= ','")
print("Nunca","pares","de","aprender\n", sep=",")

print(">>>Impresiòn de variables")
frase= "Nunca pares de aprender"
autor = "Platzi"
print("Frase:",frase,"Author:",autor,"\n")

print(">>>Uso de formato con f-string: print(f)")
print(f"Frase: {frase}, Autor:{autor}\n")

print(">>>Uso de formato con format:{}")
print("Frase: {}, Autor: {}\n".format(frase,autor))

print(">>>Uso de formato especifico")
valor=3.14159
print("Valor: {:.2f}".format(valor))







