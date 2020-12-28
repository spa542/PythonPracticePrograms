# OOP
# Creating Objects

class PlayerCharacter:
    # Class Object Attribute aka Static variable
    membership = True

    def __init__(self, name, age, confused=True):
        self.name = name # attributes
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self):
        print('run')
    
    @classmethod
    # Allow the method to be used without instantiating the class
    def adding_things(cls, num1, num2):
        return num1 + num2
    
    @classmethod
    # Access to the attributes and instantiation
    def add_stuff(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    # No access to the class attributes
    def add_more(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Cindy', 25)
player2 = PlayerCharacter('Tom', 31)

print(player1)
print(player1.name)
print(player1.age)
print(player2)
print(player2.name)
print(player2.age)
player1.run()
player2.run()
PlayerCharacter.membership = False
print(player1.membership)
print(player2.membership)
# Using classmethod decorator
print(player1.adding_things(2,3))
player3 = PlayerCharacter.add_stuff(1,5)
print(player3.age)
