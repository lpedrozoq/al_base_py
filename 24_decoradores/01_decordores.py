print()
print(">>>>Decoradores")
print()

print(">>1- Ejemplo antes de decoradore: def saludar() || def super_funcion(funcion) ")

def saludar():
    print("Hola!, soy una función")
    
def super_funcion(funcion):
    funcion()

#Asignamos la función a un variable
funcion = saludar        

super_funcion(funcion)
print()

print(">>2- Aplicando decoradores: modificar el comportamiento de una fnc existente")
def funcion_a(funcion_b):
    def funcion_c():
        print("Antes de la ejecución de la función a decorar")
        funcion_b()
        print("Después de la ejecución de la función a decorar")
    return funcion_c
    
@funcion_a
def saludarV2():
    print("Hola mundo!!")    

saludarV2()    
print()

print(">>3- Aplicando decoradores: cuando la función tiene argumentos: def suma(1,2)")
def funcion_a1(funcion_b1):
    def funcion_c1(*args, **kwargs):
        print("Antes de la ejecución de la función  decorar")
        result = funcion_b1(*args, **kwargs)
        print("Después de la ejecución de la función  decorar")    
        return result
    return funcion_c1

@funcion_a1
def suma(a,b):
    return a + b

print(suma(3,4))
print()







