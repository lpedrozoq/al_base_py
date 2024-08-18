import csv
print()
print(">>>>Leyendo archivo csv")
print()

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',') 
        #Se itera par leer fila a fila
        print("%%%" * 5)
        for row in reader:
            print("***" * 5)
            #Cada fila se imprime como una lista
            #El resto es imprimirlo como un lista de diccionarios
            print(row)
        

if __name__ == "__main__":
    read_csv("./21_archivos/data.csv")    