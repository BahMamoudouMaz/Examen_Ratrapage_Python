import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def draw(self):
        t = turtle.Turtle()
        t.fillcolor("black")  # Fond noir
        t.begin_fill()
        t.color("red")  # Bordure rouge
        for _ in range(2):
            t.forward(self.longueur)
            t.left(90)
            t.forward(self.largeur)
            t.left(90)
        t.end_fill()
        turtle.done()

class Square(Rectangle):
    def __init__(self, cote, inclinaison=30):
        super().__init__(cote, cote)
        self.inclinaison = inclinaison

    def draw(self):
        t = turtle.Turtle()
        t.fillcolor("black")  # Fond noir
        t.begin_fill()
        t.color("red")  # Bordure rouge
        t.left(self.inclinaison)  # Inclinaison initiale
        for _ in range(4):
            t.forward(self.longueur)
            t.left(90)
        t.end_fill()
        turtle.done()

# Exemple d'utilisation
rectangle1 = Rectangle(100, 50)
rectangle1.draw()

square1 = Square(100)
square1.draw()

