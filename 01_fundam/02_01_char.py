"""
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1  
"""

#Caracter posiciòn 
word = "Python"
print("\n")
print(word[0])
print("\n")

#Indices may also be negative numbers, to start counting from the right:
print(word[-1])
print(word[-6])
print("\n")

#slicing
#Characters from position 0 (included) to 2 (excluded)
print(word[0:2])
print(word[2:5])
