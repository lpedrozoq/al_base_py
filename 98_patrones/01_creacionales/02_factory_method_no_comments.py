from __future__ import annotations
from abc import ABC, abstractmethod

"""
Creator (Clase Abastracta)
"""
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


"""
Product (Clase abstracta)
"""
class Product(ABC):
    @abstractmethod
    def operation(self)-> str:
        pass


"""
ConcreteCreator1
"""
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()
    
        
"""
ConcreteCreator2
"""
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
    

    

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"    

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"    

def client_code(creator : Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.{creator.some_operation()}")    
    
if __name__ == "__main__":
    print()
    print(">>>>Factory mehtod")
    print()
    print(">1-App: launched with the ConcreteCreator1")
    client_code(ConcreteCreator1())
    print()
    print(">2-App: launched with the ConcreteCreator2")
    client_code(ConcreteCreator2())
    print()
        
      
