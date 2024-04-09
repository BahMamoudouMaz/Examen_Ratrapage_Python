from math import gcd

class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def invert(self):
        return Fraction(self.denominateur, self.numerateur)

    def simplify(self):
        gcd_value = gcd(self.numerateur, self.denominateur)
        return Fraction(self.numerateur // gcd_value, self.denominateur // gcd_value)

    def __mul__(self, other):
        return Fraction(self.numerateur * other.numerateur, self.denominateur * other.denominateur)

    def __add__(self, other):
        return Fraction(self.numerateur * other.denominateur + other.numerateur * self.denominateur,
                        self.denominateur * other.denominateur)

    def __sub__(self, other):
        return Fraction(self.numerateur * other.denominateur - other.numerateur * self.denominateur,
                        self.denominateur * other.denominateur)

    def __truediv__(self, other):
        return Fraction(self.numerateur * other.denominateur, self.denominateur * other.numerateur)

    def __str__(self):
        return f"{self.numerateur}/{self.denominateur}"

    @classmethod
    def from_string(cls, fraction_string):
        numerateur, denominateur = map(int, fraction_string.split('/'))
        return cls(numerateur, denominateur)

def main():
    f1 = Fraction(2, 4)
    f2 = Fraction(1, 4)
    f3 = f1 + f2
    f4 = f1 - f2
    f5 = f1 * f2
    f6 = f1 / f2
    f7 = Fraction(4, 10)
    f8 = Fraction.from_string('5/10')

    print(f3)            # affiche: 3/4
    print(f4)            # affiche: 1/4
    print(f5)            # affiche: 1/8
    print(f6)            # affiche: 2
    print(f7.simplify()) # affiche: 2/5
    print(f7.invert())   # affiche: 10/4
    print(f8)            # affiche: 5/10

main()
