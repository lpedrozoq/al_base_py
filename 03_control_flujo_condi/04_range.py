print()    
print(">>> for i in range(5)")
for i in range(5):
    print(i)

print()    

print(">>> list(range(5,10))")
list1 = list(range(5,10))
print(list1)

print()    

print(">>> list(range(0,10,3))")
list2 = list(range(0,10,3))
print(list2)

print()   

print(">>> list(range(-10,-100,-03))")
list3 = list(range(-10,-100,-30))
print(list3)

print()   

#Iterar sobre el índice de un secuencia:
print(">>> ['Mary','Had','A','LITTEL','LAMB']")
a = ['Mary','Had','A','LITTEL','LAMB']
for i in range(len(a)):
    print(i,a[i])        

print()

print(">>> sum(range(4)): 0 + 1 + 2 + 3")
val : int = sum(range(4)) #interesante entender cómo funciona esta parte
print(val)


      
