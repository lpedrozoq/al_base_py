print()
print(">>>>Abstract classes")
print()

print(">1- Sin abstract classes")

class LionV1:
    def give_food(self):
        print("Feeding lion with raw meat")

class PandaV1:
    def feed_animal(self):
        print("Feeding a panda with some tasty bamboo!")

class SnakeV1:
    def feed_snake(self):
        print("Feeding a snake with mice!")
        
#Animals for zoo:
leo = LionV1()
po = PandaV1()
sam = SnakeV1()    

leo.give_food()
po.feed_animal()
sam.feed_snake()
print()    

print(">2- Con abstract classes ")
# abc is a builtin module, we have to import ABC and abstractmethod
from abc import ABC, abstractmethod

# Inherit from ABC(Abstract base class)
class Animal(ABC):
    # Decorator to define an abstract method
    @abstractmethod
    def feed(self):
        pass
    
class LionV2(Animal):
    def feed(self):
        print("Feeding lion with raw meat")

class PandaV2(Animal):
    def feed(self):
        print("Feeding a panda with some tasty bamboo!")

class SnakeV2(Animal):
    def feed(self):
        print("Feeding a snake with mice!")

zoo = [LionV2(), PandaV2(), SnakeV2()]
for animal in zoo:
    animal.feed()        
print()    