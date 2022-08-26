class Complex:
    def __init__(self, a, b):
        self.re = a
        self.im = b

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __repr__(self):
        return f"{self.re} + {self.im}i" if self.im > 0 else f"{self.re} - {abs(self.im)}i"


if __name__ == "__main__":
    c_1 = Complex(a=2, b=3)
    c_2 = Complex(a=1, b=4)
    print(c_1*c_2)
