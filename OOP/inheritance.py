class Car: 
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")
# creating a subclass
class BMW(Car):
    def __init__(self, name):
        self.name = name

car1 = BMW("X5")
car2 = BMW("X3")
print(car1.start())
car2.stop()   # inherited method

#3 type of inheritance: 1. single inheritance 2. multilevel inheritance 3. hierarchical/multiple inheritance
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):   # single inheritance
    def bark(self):
        print("Dog barks")      
class Puppy(Dog):   # multilevel inheritance
    def weep(self):
        print("Puppy weeps")
class Cat(Animal):   # hierarchical inheritance
    def meow(self):
        print("Cat meows")

dog1 = Dog()
dog1.speak()   # inherited method
dog1.bark()
puppy1 = Puppy()
puppy1.speak()   # inherited method
puppy1.bark()    # inherited method
puppy1.weep()
cat1 = Cat()
cat1.speak()   # inherited method
cat1.meow()


#multiple inheritance
class Father:
    def skills(self):
        print("Gardening, Programming")
class Mother:
    def skills(self):
        print("Cooking, Art")
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports, Music")
child1 = Child()
child1.skills()

        