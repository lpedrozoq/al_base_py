import modules_custom

print()
print(">>>Module cli #1")
print()

print("1- Invocar todo un modulo y un mètodo en particular")
print(modules_custom.get_population())
print()

print("2- Invocar todo un modulo y otro mètodo en particular")
data = [
        {
            "Country":"Colombia",
            "Population":500
        },
        {
            "Country":"Bolivia",
            "Population":300
            
        }
    ]
result = modules_custom.get_population_by_country(data,"Colombia")
print(result)
print()

print("3- pidiendo el país:")
input = input("Digite el país ")
result = modules_custom.get_population_by_country(data,input)
print(result)
print()


