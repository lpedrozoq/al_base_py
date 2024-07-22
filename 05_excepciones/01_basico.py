print()
print(">>>try-except")

try:
    x = 1  
    x = 1/0
    print(x)
except:
    print('An exception occurred')
    print()