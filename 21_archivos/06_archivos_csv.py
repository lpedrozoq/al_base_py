import csv
print()
print(">>>>Leyendo archivo csv")
print()


def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',') 
        #Se itera par leer fila a fila
        #Como el 'reader' es un iterable, ahi podemos
        #traer màs info como los nombres de la columnas
        print("%%%" * 5)
        header = next(reader)
        data = []
        for row in reader:
            print("***" * 5)
            iterable = zip(header,row)
            country_dict = {key : value for  key, value in iterable}
            #print(country_dict)
            data.append(country_dict)
        return data    
        

if __name__ == "__main__":
    data = read_csv("./21_archivos/data.csv")    
    print(data)