print()
print(">>>Errores")
print()

print("1- Division por cero")
try:
  print(0/0)
except ZeroDivisionError as error:
  print('**** Excepciòn: ', error)
print()