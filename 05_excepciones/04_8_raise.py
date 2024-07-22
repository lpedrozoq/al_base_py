print("===Raise Exceptions===")
print()

try:
    raise Exception("Spam","Eggs")
except Exception as inst:
    print("type(e): ",type(inst))   #the exception type
    print("e.args: ",inst.args)    #args stored in .args
    print("e: ", inst)         #__str__ allows args to be printed directly
    x,y = inst.args     #unpack args
    print("x (x,y = e.args)=",x)
    print("y (x, y = e.args)",y)
    