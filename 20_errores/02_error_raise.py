print()
print(">>>Errores: lanzando error")
print()

print("1- Lanzando error con raise")
age = 10
if age < 18:
    raise Exception("age no es mayor que 18")
print()