# Encapsulation and Abstraction
# Public and Private Usage
# - put an underscore in front to "say" that it is private
# - there is no true privacy in python

class PlayerCharacter:
    def __init__(self, name, age): # Dunder method
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old')

player1 = PlayerCharacter('Ryan', 100)
player1.speak()


