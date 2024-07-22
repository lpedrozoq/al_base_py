print("===Exceptions/Finally===")
print()

try:
    #f = open("/demofile.txt")
    x = 1/1
    try:
        #f.write("Eliachito")
        y = 1/0
    except:
        print("Something went wrong writing to the file")    
    finally:
        #f.close()    
        print("Finally")    
except:
    print("Something went wrong when opening the file")    