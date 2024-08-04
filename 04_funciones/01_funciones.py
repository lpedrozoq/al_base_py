print()
print(">>>Funciones")
print()


print("1- greet()")
def greet():
    print("Hola mundo")
greet()

print()

print("2- greet(name)")
def greet(name):
    print(name)
greet("Claudia Fda.")    

print()

print("3- greet(name,last_name)")
def greet(name,last_name):
    print(f"name: {name} and last name: {last_name}")
greet("Angela","Pedrozo")    

print()

print("4- greet(name,last_name)")
def greet_news(name,last_name="<<No tiene apellido>>"):
    print(f"greet: name: {name} and last name: {last_name}")
greet_news("Rebeca")    
print()

print("5- sum_with_range(min, max)")
def sum_with_range(min,max):
    sum = 0
    for item in range(min,max):
        sum += item
    print(sum)
sum_with_range(1,5)    
print()    
     
print("6- get_sum_with_range(min, max)")
def get_sum_with_range(min,max):
    sum = 0
    for item in range(min,max):
        sum += item
    return sum
print(get_sum_with_range(1,5))
print()    




