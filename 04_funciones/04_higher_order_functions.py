print()
print(">>>Higher order functions")
print()

print("1-hihg_ord_func(x,func)  (donde 'func' es otra funciòn(usa v1))")
def increment_v1(x):
    return x + 1
def hihg_ord_func_v1(x,func):
    return x + func(x)
result = hihg_ord_func_v1(2,increment_v1)
print(result)
print()

print("2-hihg_ord_func_v2(x,func)  (donde 'func' es otra funciòn(usa v2))")
increment_v2 = lambda x : x + 1
def hihg_ord_func_v2(x,func):
    return x + func(x)
result = hihg_ord_func_v2(3,increment_v2)
print(result)
print()

print("3-hihg_ord_func_v3(x,func)  (donde 'func' es otra funciòn(usa v2))")
hihg_ord_func_v3 = lambda x, func: x + func(x)
print(hihg_ord_func_v3(4,increment_v1))
print(hihg_ord_func_v3(4, lambda x : x*2))
print()