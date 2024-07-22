def print_exception_hierarchy(excepction_class, indent= 0):
    print(" " * indent + excepction_class.__name__)
    for subclass in excepction_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

#Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)        