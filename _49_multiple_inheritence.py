# multiple inheritance = inherit from more than one parent class
#                       C(A, B)
#
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This animal {self.name} is eating")

    def sleep(self):
        print(f"This animal {self.name} is sleeping")


#
class Prey(Animal):
    def flee(self):
        print(f"This animal {self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"This animal {self.name} is hunting")


# children class
class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Momo")
hawk = Hawk("Aero")
fish = Fish("Gold")

rabbit.flee()
# hawk.flee()       'Hawk' object has no attribute 'flee'
fish.flee()

# rabbit.hunt()      'Rabbit' object has no attribute 'hunt'
hawk.hunt()
fish.hunt()

rabbit.eat()
hawk.eat()
fish.eat()

rabbit.sleep()
hawk.sleep()
fish.sleep()
