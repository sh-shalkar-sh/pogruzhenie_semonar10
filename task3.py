class Triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def set_sides(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b

    def triangle_type(self):
        if not self.is_valid():
            return "Треугольника с такими сторонами не существует"
        elif self.a == self.b == self.c:
            return "Треугольник является равносторонним"
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "Треугольник является равнобедренным"
        else:
            return "Треугольник является разносторонним"


triangle = Triangle()


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))


triangle.set_sides(a, b, c)

print(triangle.triangle_type())
