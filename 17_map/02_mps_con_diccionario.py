print()
print(">>>Map: maps con diccionarios (WOOOOWWWW!!!)")
print()

print("1-Obtener de una lista de diccionarios un valor puntual y convertirla a una list de precios")
items = [
    {
        "product":"camis",
        "price":"100"
    },
    {
        "product":"pantalones",
        "price":"300"
    },
    {
        "product":"pantalones 2",
        "price":"200"
    }
]
#Ej: price = [100,300,200]
prices = list(map(lambda item : item["price"], items))
print(prices)
print()


print("2-Generar un nuevo atributo en la lista-dicc")
items1 = [
    {
        "product":"camis",
        "price":100
    },
    {
        "product":"pantalones",
        "price":300
    },
    {
        "product":"pantalones 2",
        "price":200
    }
]

def add_taxes(item):
    item["taxes"] = item["price"] * .19
    return item
new_items = list(map(add_taxes, items1))
print(new_items)
print()