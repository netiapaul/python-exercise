# finding the area and circumfrence

class Circle():
    """initializing a class ciricle"""
    def __init__(self,radius):
        """initializing area and circumfrence"""
        self.radius=radius
       
    def get_area(self):
        area=(3.14*self.radius*self.radius)
        print(area)

    def get_circumfrence(self):
        circumfrence=(self.radius*2*3.14)
        print(circumfrence)
        
circle=Circle(20)
circle.get_area()
circle.get_circumfrence()

# converting celsius to faranheit and vice-versa

class Temparature():
    """creating temparature class"""
    def __init__(self,celcius,faranheight):
        self.celcius=celcius
        self.faranheight=faranheight

    def convertFahrenheit(self):
        """converts celcius to faranheight"""
        faranheit=((self.celcius*(9/5))*32)
        print(faranheit)

    def convertCelsius(self):
        """convert to celsius"""
        convcelsius=(self.faranheight-32)*(5/9)
        print(convcelsius)

temp=Temparature(30,45)
temp.convertCelsius()
temp.convertFahrenheit()

# class of a pupil in a school

class Student():
    """initializing a student class"""
    def __init__(self,name,roll_number):
        """initializing name with roll number"""
        self.name=name
        self.roll_number=roll_number

    def Display(self):
        """dispalys name and roll number"""
        print('the student name is: ' + self.name + ' and roll number is ' + str(self.roll_number))

    def Age(self,age):
        """initailizing the age of student"""
        self.age=age
        print('the age of the student is: ' + str(self.age))
    
    def setMarks(self,marks):
        """setting marks to students"""
        self.marks = marks
        print('The mark of the student is: ' + str(self.marks))

pupil=Student('paul',35629)
pupil.Display()
pupil.Age(10)
pupil.setMarks(69)
    
# class inheritance

class Car():
    """initializing a car model"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name.title())

my_new_car = Car('audi', 'a4', 2016)
my_new_car.get_descriptive_name()

class Electric_car(Car):
    """this class is a subclass of the superclass car"""
    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        super().__init__(make,model,year)

tesla=Electric_car('Tesla','model s',2018)
tesla.get_descriptive_name()