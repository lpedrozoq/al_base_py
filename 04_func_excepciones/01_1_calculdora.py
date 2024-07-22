print()

def suma(a,b):
    return  a+b

def resta(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print()
        print("========================")
        print("Seleccione una operacion")
        print("========================")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. salir")
        print()
        opcion = int(input("Digite opciòn (1,2,3,4,5):"))

        if opcion == 5:
            print("Saliendo de la calculadora")
            print()
            break

        if opcion in [1,2,3,4]:
            print()
            num1 = float(input("Ingrese el primer nùmero: "))
            num2 = float(input("Ingrese el segundo nùmero: "))
            print()
            if opcion == 1:
                print("La suma es: ", suma(num1,num2))
                print()
            elif opcion == 2:    
                print("La resta es: ", resta(num1,num2))
                print()
            elif opcion == 3:    
                print("La multiplicacion es: ", multiplica(num1,num2))
                print()
            elif opcion == 4:    
                print("La divisiòn es: ", divide(num1,num2))
                print()
        else:
            print("Digite una opciòn no vàlida...")
            print()
calculator()
print()
 





