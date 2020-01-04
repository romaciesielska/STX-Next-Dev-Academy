from math import pi, sqrt, tan


class Triangle:

    def __init__(self,a,h):
        self.a = a
        self.h = h

    def area(self):
        return (self.a * self.h)/2

    def __str__(self):
        print(f"Trójkąt o podstawie = {self.a} i wysokości równej = {self.h} ma pole = {self.area()}.")

triangle = Triangle(4,7)
triangle.__str__()


class Rectangle:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def __str__(self):
        print(f"Prostokąt o bokach = ({self.a}, {self.b}) ma pole = {self.area()}.")

rectangle = Rectangle(5,3)
rectangle.__str__()


class Square(Rectangle):

    def __init__(self,a):
        super().__init__(a,a)

    def __str__(self):
        print(f"Kwadrat o boku = {self.a} ma pole = {self.area()}.")

square = Square(3.5)
square.__str__()


class Cube(Square):

    def __init__(self,a):
        super().__init__(a)

    def surface_area(self):
        return 6 * self.area()

    def volume(self):
        return self.a * self.area()

    def __str__(self):
        print(f"Sześcian o boku = {self.a} ma pole powierzchni = {self.surface_area()} oraz objętość = {self.volume()}.")

cube = Cube(2)
cube.__str__()


"""
Polecenie dotyczy ostrosłupa foremnego, tj. ostrosłupa posiadającego w podstawie dowolny wielokąt foremny.
W imię ogólności, wyprowadziłam wzory na pole powierzchni i objętość dla ostrosłupa foremnego o podstawie n-kąta foremnego o boku a i danej wysokości h.
Zastosowałam w nich dość skomplikowane (znalezione w sieci) wzory na wysokość ściany bocznej oraz pole podstawy w zależności wyłącznie od parametrów n, a, h.

Gdyby jednak intencją autora zadań było zastosowanie w praktyce utworzonej wcześniej klasy dla trójkąta,
poniżej utworzyłam uproszczoną klasę dla czworościanu foremnego.
"""
class Pyramid:

    def __init__(self,n,a,h):
        self.n = n
        self.a = a
        self.h = h

    def base_area(self):
        return (self.n * (self.a ** 2) * 1/(tan(pi/self.n)))/4

    def surface_area(self):
        slant_height = sqrt((self.h ** 2) + ((self.a ** 2) * ((1/(tan(pi/self.n))) ** 2))/4 )
        side_area = (self.n * self.a * slant_height)/2
        return self.base_area() + side_area

    def volume(self):
        return (self.base_area() * self.h)/3

    def __str__(self):
        print(f"Ostrosłup foremny o podstawie {self.n}-kąta długości {self.a} i wysokości równej {self.h} ma pole powierzchni = {self.surface_area()} oraz objętość = {self.volume()}.")

pyramid = Pyramid(3,4,3.266)
pyramid.__str__()


class RegularTetrahedron(Triangle):

    def __init__(self,a):
        super().__init__(a,a*sqrt(3)/2)

    def surface_area(self):
        return 4 * self.area()

    def volume(self):
        return (self.a ** 3)/(6*sqrt(2))

    def __str__(self):
        print(f"Czworościan foremny o boku długości {self.a} ma pole powierzchni = {self.surface_area()} oraz objętość = {self.volume()}.")
    
tetrahedron = RegularTetrahedron(4)
tetrahedron.__str__()


class Ellipse:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area(self):
        return pi * self.a * self.b

    def __str__(self):
        print(f"Elipsa o półosiach = ({self.a}, {self.b}) ma pole = {self.area()}.")

ellipse = Ellipse(4,5)
ellipse.__str__()


"""
We wszystkich zadaniach przyjęłam założenie prawidłowości danych wejściowych. W prawdziwej aplikacji należałoby oczywiście dodać walidację parametrów, sprawdzając:
 - czy są liczbami typu float,
 - czy są większe od 0,
 - dla ostrosłupa foremnego: czy liczba krawędzi podstawy jest większa lub równa 3.
"""