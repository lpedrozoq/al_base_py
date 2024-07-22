class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
           self.is_available = False
           print(f":: Vehicle.sell - El vehículo {self.brand} ha sido vendido")         
        else:
           print(f":: Vehicle.sell - El vehículo {self.brand} no está disponible")                              

    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError(":: Vehicle.start_engine - Este método debe ser implementado por la sub-clase")
    
    def stop_engine(self):
        raise NotImplementedError(":: Vehicle.stop_engine - Este método debe ser implementado por la sub-clase")
    
    def check_available(self):
        return self.is_available
            

#-----------------------------------------------------
#
#-----------------------------------------------------
class Car(Vehicle):
    def __init__(self, brand, model, price):
        print("::Car()")
        super().__init__(brand, model, price)

    def start_engine(self):
        if not self.is_available:
            return f":: Car.start_engine - El motor del coche {self.brand} está en marcha"
        else:
            return f":: Car.start_engine - El motor del coche {self.brand} está detenido"

    def stop_engine(self):
        if self.is_available:
            return f":: Car.stop_engine - El motor del coche {self.brand} está detenido"
        else:
            return f":: Car.stop_engine - El motor del coche {self.brand} está en marcha"
            
#-----------------------------------------------------
#
#-----------------------------------------------------
class Bycicle(Vehicle):
    def __init__(self, brand, model, price):
        print("::Bycicle()")
        super().__init__(brand, model, price)

    def start_engine(self):
        if not self.is_available:
            return f":: Bycicle.start_engine - La bicicleta {self.brand} está en marcha"
        else:
            return f":: Bycicle.start_engine - La bicicleta {self.brand} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f":: Bycicle.stop_engine - La bicicleta {self.brand} está detenida"
        else:
            return f":: Bycicle.stop_engine - La bicicleta {self.brand} está en marcha"
            
#-----------------------------------------------------
#
#-----------------------------------------------------
class Truck(Vehicle):
    def __init__(self, brand, model, price):
        print("::Truck()")
        super().__init__(brand, model, price)

    def start_engine(self):
        if not self.is_available:
            return f":: Truck.start_engine - El camión {self.brand} está en marcha"
        else:
            return f":: Truck.start_engine - El camión {self.brand} está detenido"

    def stop_engine(self):
        if self.is_available:
            return f":: Truck.stop_engine - El camión {self.brand} está detenido"
        else:
            return f":: Truck.stop_engine - El camión {self.brand} está en marcha"


#-----------------------------------------------------
#
#-----------------------------------------------------
class Customer:
    def __init__(self,name):
        self.name = name
        self.purchased_vechicles = []

    def buy_vehicle(self, vehicle : Vehicle):
        if vehicle.is_available:
            vehicle.sell()
            self.purchased_vechicles.append(vehicle)
        else:
            print(f"Los siento, {vehicle.brand} no está disponible")

    def inquire_vechicle(self, vehicle : Vehicle):
        if vehicle.check_available():
            availability = "Disponible" 
        else:
            availability = "No disponible"   
        print(f"El {vehicle.brand} está {availability} y cuesta {vehicle.get_price()}")              

#-----------------------------------------------------
#
#-----------------------------------------------------
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle : Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer : Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")                

    def show_available_vehicle(self):
        print("Vehículos disponibles en la tienda")        
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")


# ****************************************************************
# ****************************************************************
                
car1 = Car("Toyota","Corolla",20000) 
bike1 = Bycicle("Yamaha","MT-07",7000)    
truck1 = Truck("Volvo","FH16",80000)

customer1 = Customer("Carlos")

dl = Dealership()
dl.add_vehicle(car1)
dl.add_vehicle(bike1)
dl.add_vehicle(truck1)

#Mostrar vehículos disponibles
dl.show_available_vehicle()

#Client consultar un vehículo
customer1.inquire_vechicle(car1)
customer1.buy_vehicle(car1)



