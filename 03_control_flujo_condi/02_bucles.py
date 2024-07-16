numbers = [1,2,3,4,5,6]
for i in numbers:
    print("Aquí i es iguala a:",i)

print()

for i in range(10):
    print("Rango...i: ", i)    

print()

fruits = ["Manzana","Pera","Uva","Tomate"]
for fruit in fruits:
    if fruit == "Pera":
        print("Naranja encontrada")            
        break
    else:
        print("Fruit: ", fruit)

print()

x = 1
while(x < 5):
    print(x)
    x += 1

print()

#Estrategia: itera sobre una copia
print(">>>Crea un copia colección")
users = {'Hans':'Activate','Leo': 'Inactivate', 'Abel':'Activate'}
print(users)
for user, status in users.copy().items():
    if status == 'Inactivate':
        del users[user]
print(users)

print()

#Estrategia: crea una colección
print(">>>Crea un copia colección")
activate_users = {}
for user, status in users.items():
    if status == 'Activate':
        activate_users[user] = status
print(activate_users)        

    





