print()
print(">>>Funciones: mùltiples retornos, etc")
print()

print("1- Paràmetros normales: find_volume(lenth, width, depth)")
def find_volume_v1(lenth, width, depth):
    return lenth * width * depth
result = find_volume_v1(10,20,3)
print(result)
print()

print("2- Paràmetros por defecto: find_volume_v2(lenth=1, width=1, depth=1)")
def find_volume_v2(lenth = 1, width =1, depth=1):
    return lenth * width * depth
result = find_volume_v2()
print(result)
print()

print("3- Paràmetros por defecto(usando un sòlo parm): find_volume_v2(lenth=1, width=1, depth=1)")
result = find_volume_v2(width=2)
print(result)
print()

print("4- Paràmetros por defecto (retornando varios valores): find_volume_v3(lenth=1, width=1, depth=1)")
def find_volume_v3(lenth = 1, width =1, depth=1):
    return lenth * width * depth, width, "Hola v3"
#Se obtiene una tupla (por defecto)
result = find_volume_v3()
print(result)
print("Imprimiendo un sòlo valor de esa tupla: result[0]")
print(result[0])
print(result[1])
print(result[2])
print()


print("5- Paràmetros por defecto 'con casting' (retornando varios valores en un set): (lenth : int = 1, width : int =1, depth : int =1)")
def find_volume_v4(lenth : int = 1, width : int =1, depth : int =1):
    #Noto que que el width no carga por defecto en un set
    return {lenth * width * depth, width, "Hola v4"}
#Se obtiene un Set
result_v4 = find_volume_v4()
print(result_v4)
print()

print("6- Paràmetros por defecto 'con casting' (retornando varios valores en un list): (lenth : int = 1, width : int =1, depth : int =1)")
def find_volume_v5(lenth : int = 1, width : int =1, depth : int =1):
    return [lenth * width * depth, width, "Hola v5"]
#Se obtiene un Set
result_v5 = find_volume_v5()
print(result_v5)
print()




