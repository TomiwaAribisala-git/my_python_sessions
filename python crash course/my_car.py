from car import Car, ElectricCar # importing class

my_old_car = Car('toyota', 'camry', 2010)
print(my_old_car.get_descriptive_name())
print(my_old_car.read_odometer())
my_new_car = Car('toyota', 'muzzle', 2020)
my_new_car.update_odometer(44) # modifying an attribute value through a method 
print(my_new_car.read_odometer())
print(f"The {my_new_car.year} {my_new_car.make} is parked at Afrikan Lane.") # accessing attributes 

my_telsa = ElectricCar('dodge', 'challenger', 2015)
print(my_telsa.get_descriptive_name())