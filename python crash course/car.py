# This file is a module. 
# A module should have a docstring describing what the classes in the module can be used for. 
# storing multiple classes in a module, you can store as many classes in a module,
# although each class in a module should be somehow related.
# within a module, you can use two blank lines to separate classes. 

"""This classes represents a car and it's features"""
class Car: 
    """A simple statement to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 23 # setting a default value for odometer_reading attribute
                                   # Attributes can be defined without being passed in as, 
                                   # parameters, these can attributes can be defined in the init method.
    def get_descriptive_name(self): 
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Return a car odometer number."""
        sup_name = f"My old car has {self.odometer_reading} miles on it!"
        return sup_name.title()

    def update_odometer(self, mileage):  # modifying an attribute value through a method 
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage


"""This classes represents a car and it's features"""
class ElectricCar(Car): # when you write a child class, the parent class, 
                        # must be part of the current file and must appear, 
                        # before the child class in the file.
    """Represent aspects of a electric car"""

    def __init__(self, make, model, year): # the init method
        """Intialize attributes of the parent class
        Then initialize attributes specific to a electric car"""
        super().__init__(make, model, year) # this super() function is a special function that allows, 
                                            # you to call a method from the parent class
                                            # This line tells Python to call the __init__() method from Car
                                            # which gives an ElectricCar instance all the attributes 
                                            # defined in the init method.
        # self.battery_size = 75 # This attribute will be associated with all instances created from, 
                                 # the ElectricCar but won't be associated with any instances of Car.
        # def describe_battery(self):
        # """Print a statement describing the battery size."""
        # print(f"This car has a {self.battery_size}-kWh battery.")
        self.battery = Battery() # instances as atrributes 


class Battery: # instances as attributes 
    """A simple battery case of an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size 

    def describe_battery(self):
        """Return the battery size of an electric car"""
        bat_size = f"This car has a {self.battery_size} Kwh capacity."
        return bat_size 
    
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
    print(f"This car can go about {range} miles on a full charge.")

my_telsa = ElectricCar('dodge', 'challenger', 2015) # testing inheritance
print(my_telsa.get_descriptive_name()) # testing inheritance
print(my_telsa.battery.describe_battery())
my_telsa.get_range()