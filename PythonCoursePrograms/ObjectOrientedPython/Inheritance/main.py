# Inheritance
# How to user super()!!!!

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do nothing')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left-{self.num_arrows}')

wizard1 = Wizard('Merlin', 50, '@gmail')
archer1 = Archer('Robin', 100, '@gmail')
wizard1.sign_in()
archer1.sign_in()
wizard1.attack()
archer1.attack()

# This is because of Polymorphism!!!!!!!
for char in [wizard1, archer1]:
    char.attack()
print(isinstance(wizard1, Wizard))

# Used for introspection - Determining what the objects has access to
# print(dir(wizard1))

# Dunder Methods __MethodName__ methods

class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = { 'name': 'Yoyo', 'has_pets': False }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('Deleted!')

    def __call__(self):
        return 'yesss?'
    
    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
