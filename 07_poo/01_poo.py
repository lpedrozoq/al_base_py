class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hola mi nombre es {self.name} y tengo {self.age}")
    def __str__(self):
        return f"{self.name}, {self.age}"
    def  __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
        

p1 = Person("Leo",45)
p2 = Person("Claudia",41)  
p1.greet()
p2.greet()      
print(p1)
print(repr(p1))
print()
print("<<--->>")
print()
class BankAccount:
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance =+ amount
            print(f"deposito :: se ha depositado {amount} y el saldo actual es {self.balance}")
        else:
            print("deposito :: no se puede en cuenta inactiva")            

    def withdrwaw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance =- amount
                print(f"withdrwaw :: se ha retirado {amount}. Saldo actual {self.balance}") 

    def deactivate_account(self):
        self.is_active = False
        print("deactivate_account :: la cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print("activate_account :: la cuenta ha sido activada")

c1 = BankAccount("Ana",500) 
c2 = BankAccount("Luis",1000) 

print()
print (">>>> POO")
print()

c1.deposit(200)
c2.deposit(100)
c1.deactivate_account()
c1.deposit(50)



