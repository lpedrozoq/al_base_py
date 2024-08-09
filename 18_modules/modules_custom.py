def get_population():
    key = ['col','bol','ven']
    values = [100,200,300]
    return key,values

def get_population_by_country(data,country):
    result = list(filter(lambda item :
        item["Country"] == country,data))
    return result

