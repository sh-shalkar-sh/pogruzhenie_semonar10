class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec

    @classmethod
    def create_pet(cls, pet_type, name, age, spec):
        if pet_type == 'Dog':
            return Dog(name, age, spec)
        elif pet_type == 'Cat':
            return Cat(name, age, spec)
        elif pet_type == 'Bird':
            return Bird(name, age, spec)
        else:
            raise ValueError("Неизвестный тип домашнего животного")

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

pet1 = Animal.create_pet('Dog', 'Bob', 5, 'гавкает')
pet2 = Animal.create_pet('Cat', 'Felix', 2, 'мурлыкает')
pet3 = Animal.create_pet('Bird', 'Aro', 1, 'поет')

for pet in [pet1, pet2, pet3]:
    print(f'{pet.name} {pet.get_spec()}')
