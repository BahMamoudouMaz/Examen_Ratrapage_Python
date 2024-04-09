import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def tracer_figure(self):
        t = turtle.Turtle()
        t.color("red")  # Couleur du premier côté
        t.forward(self.longueur)
        t.left(90)
        t.color("blue")  # Couleur du deuxième côté
        t.forward(self.largeur)
        t.left(90)
        t.color("green")  # Couleur du troisième côté
        t.forward(self.longueur)
        t.left(90)
        t.color("orange")  # Couleur du quatrième côté
        t.forward(self.largeur)
        t.left(90)
        turtle.done()

# Exemple d'utilisation
rectangle1 = Rectangle(100, 50)
rectangle1.tracer_figure()


