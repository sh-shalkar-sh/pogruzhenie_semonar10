class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec

class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

class Bird(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


pet1 = Dog('Bob', 5, 'гавкает')
pet2 = Cat('Felix', 2, 'мурлыкает')
pet3 = Bird('Aro', 1, 'поет')

for pet in [pet1, pet2, pet3]:
    print(f'{pet.name}',pet.get_spec())