print()
print(">>>try-except(ValueError/ZeroDivisionError)")
print()

try:
    x = int(input("Digite un nùmero: "))
    print(x)
    x = 1/0
except ValueError:
    print('Digite un nùmero correcto')
    print()
except ZeroDivisionError:
    print('Divisiòn por cero invàlida')
    print()
        