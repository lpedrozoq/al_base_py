print()
print(">>>>Scope")
print()

price = 100 #global

def increment():
    price = 0
    price  = price + 10
    print("price (internal): ",price)
increment()
print("price: (external): ",price)    
print()    