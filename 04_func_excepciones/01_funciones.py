print()
print(">>>greet()")
def greet():
    print("Hola mundo")
greet()

print()

print(">>>greet(name)")
def greet(name):
    print(name)
greet("Claudia Fda.")    

print()

print(">>>greet(name,last_name)")
def greet(name,last_name):
    print(f"name: {name} and last name: {last_name}")
greet("Angela","Pedrozo")    

print()

print(">>>greet(name,last_name)")
def greet_news(name,last_name="<<No tiene apellido>>"):
    print(f"greet: name: {name} and last name: {last_name}")
greet_news("Rebeca")    

print()

