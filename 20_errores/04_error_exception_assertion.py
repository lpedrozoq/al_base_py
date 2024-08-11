print()
print(">>>Errores")
print()

print("1- Assert")
try:
  assert 1 != 1, "Uno no es igual que uno"
except AssertionError as error:
  print('**** Excepciòn: ', error)
finally:
  print("Controlado el assert")
print("...se puede continuar!")  
print()