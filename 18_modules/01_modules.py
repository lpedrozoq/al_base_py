print()
print(">>>Modules")
print()

import sys
print("1- Uso de import es sys")
print(sys.path)
print()

import re
print("2- import re (Regular Expresions)")
text = 'Mi numero de telefono es 311 123 121 el ccoigo del pais 57, mi npumero de la suerte es 3'
result = re.findall("[0-9]+",text)
print(result)
print()

import time
print("3- import time")
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(local)
print(result)
print()

import collections
print("4- import collections")
numbers = [1,2,3,4,5,1,1,2,3,4,5,6,1,2,3]
counter = collections.Counter(numbers)
print(counter)
print()

