print()
print("===Many exceptions===")
print()
try:
    #Variable no definida
    print(x)
#Excepción más específica
except NameError:
    print("Variable x is not defined")
    print()
#Exception general    
except:
    print("Something else went wrong")
    print()

