class MyNumbers:
    def __iter__(self):
      self.a = 1
      return self
  
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
print()
myClass = MyNumbers()
myIter = iter(myClass)
for x in myIter:
    print(x)
print()  