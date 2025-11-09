# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibility
# class Child(Parent)   sub(super)


class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    def speak(self):
        print("Meowwwww!!")

class Mouse(Animal):
    def speak(self):
        print("Chi chi!!")
    
dog = Dog("Tony")
cat = Cat("Tom")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()