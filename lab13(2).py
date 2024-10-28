import math

class TRIANGLE:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.S = 0

    def is_set(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def calc_square(self):
        if self.is_set():
            s = (self.a + self.b + self.c) / 2
            self.S = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        else:
            self.S = 0

    def show_square(self):
        self.calc_square()
        print(f"Площа трикутника: {self.S:.2f}")

    def show_dim(self):
        print(f"Розміри трикутника: a = {self.a}, b = {self.b}, c = {self.c}")

triangles = [
    TRIANGLE(3, 4, 5),
    TRIANGLE(5, 12, 13),
    TRIANGLE(7, 24, 25),
    TRIANGLE(6, 8, 10)
]

for triangle in triangles:
    triangle.show_dim()
    triangle.show_square()
    print()
