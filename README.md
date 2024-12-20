# RETO-4-POO



# SHAPE


El código trabajado en clase implementa un sistema jerárquico para representar formas geométricas mediante herencia y polimorfismo. Define una clase base Shape que incluye atributos genéricos como vértices, aristas y ángulos internos, así como métodos para calcular área, perímetro y ángulos internos. Sobre esta base, se crean clases específicas como Rectangle, Square, y diversas variantes de triángulos (Triangle, Scalene, Equilateral, Isosceles, y TriRectangle). Estas clases especializadas implementan los métodos de cálculo y personalizan atributos según las propiedades de cada forma. También incluye clases auxiliares como Point para coordenadas y Line para representar aristas. El sistema es flexible y permite modelar y calcular propiedades geométricas de diferentes formas.
``` python
import math

class Shape:
    def __init__(self, is_regular: bool = False, vertices: list = [], edges: list = [], inner_angles: list = []):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = edges
        self.inner_angles = inner_angles

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def compute_distance(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5


class Line:
    def __init__(self, start: Point = Point(), end: Point = Point()):
        self.start = start
        self.end = end
        self.length = self.compute_length()

    def compute_length(self):
        return ((self.start.x - self.end.x)**2 + (self.start.y - self.end.y)**2)**0.5


class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        super().__init__(is_regular=True)
        self.width = width
        self.height = height
        self.vertices = self.compute_vertices()
        self.edges = self.compute_edges()

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_vertices(self):
        return [Point(0, 0), Point(self.width, 0), Point(self.width, self.height), Point(0, self.height)]
    def compute_inner_angles(self):
        return [90, 90, 90, 90]
    def compute_edges(self):
        vertices = self.compute_vertices()
        edges = []
        for i in range(4):
            edges.append(Line(vertices[i], vertices[(i + 1) % 4]))
        return edges
    def __str__(self):
        vertices_str = ', '.join([f"({v.x}, {v.y})" for v in self.vertices])
        edges_str = ', '.join([f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" for e in self.edges])
        inner_angles_str = ', '.join([f"{angle:.2f}" for angle in self.compute_inner_angles()])
    
        return (f"Rectangle:\n"
            f"  Width: {self.width}\n"
            f"  Height: {self.height}\n"
            f"  Area: {self.compute_area()}\n"
            f"  Perimeter: {self.compute_perimeter()}\n"
            f"  Vertices: {vertices_str}\n"
            f"  Edges: {edges_str}\n"
            f"  Inner Angles: {inner_angles_str}")


class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(width=side, height=side)
        self.is_regular = True
    def __str__(self):
        vertices_str = ', '.join([f"({v.x}, {v.y})" for v in self.vertices])
        edges_str = ', '.join([f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" for e in self.edges])
        inner_angles_str = ', '.join([f"{angle:.2f}" for angle in self.compute_inner_angles()])
    
        return (f"Square:\n"
            f"  Side: {self.width}\n"
            f"  Area: {self.compute_area()}\n"
            f"  Perimeter: {self.compute_perimeter()}\n"
            f"  Vertices: {vertices_str}\n"
            f"  Edges: {edges_str}\n"
            f"  Inner Angles: {inner_angles_str}")


class Triangle(Shape):
    def __init__(self, base=0, height=0, side1=0, side2=0, side3=0):
        super().__init__(is_regular=False)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.vertices = self.compute_vertices()
        self.edges = self.compute_edges()

    def compute_area(self):
        return 0.5 * self.base * self.height

    def compute_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def compute_vertices(self):
        return [Point(0, 0), Point(self.base, 0), Point(self.base / 2, self.height)]

    def compute_edges(self):
        vertices = self.compute_vertices()
        edges = []
        for i in range(3):
            edges.append(Line(vertices[i], vertices[(i + 1) % 3]))
        return edges

    def compute_inner_angles(self):
        # Implementación genérica para calcular los ángulos internos de un triángulo
        a, b, c = self.side1, self.side2, self.side3
        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180 - angle_A - angle_B
        return [angle_A, angle_B, angle_C]
    
    def __str__(self):
        vertices_str = ', '.join([f"({v.x}, {v.y})" for v in self.vertices])
        edges_str = ', '.join([f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" for e in self.edges])
        inner_angles_str = ', '.join([f"{angle:.2f}" for angle in self.compute_inner_angles()])
    
        return (f"Triangle:\n"
            f"  Base: {self.base}\n"
            f"  Height: {self.height}\n"
            f"  Side1: {self.side1}\n"
            f"  Side2: {self.side2}\n"
            f"  Side3: {self.side3}\n"
            f"  Area: {self.compute_area()}\n"
            f"  Perimeter: {self.compute_perimeter()}\n"
            f"  Vertices: {vertices_str}\n"
            f"  Edges: {edges_str}\n"
            f"  Inner Angles: {inner_angles_str}")

class Scalene(Triangle):
    def __init__(self, base=0, height=0, side1=0, side2=0, side3=0):
        super().__init__(base=base, height=height, side1=side1, side2=side2, side3=side3)
        self.is_regular = False
def compute_vertices(self):
        # Using the law of cosines to find the coordinates of the third vertex
        A = Point(0, 0)
        B = Point(self.base, 0)
        cos_angle_C = (self.side1**2 + self.side2**2 - self.side3**2) / (2 * self.side1 * self.side2)
        sin_angle_C = (1 - cos_angle_C**2)**0.5
        C = Point(self.side1 * cos_angle_C, self.side1 * sin_angle_C)
        return [A, B, C]

class Equilateral(Triangle):
    def __init__(self, side=0):
        height = (side * (3**0.5)) / 2
        super().__init__(base=side, height=height, side1=side, side2=side, side3=side)
        self.is_regular = True

    def compute_area(self):
        return (self.side1**2 * (3**0.5)) / 4

    def compute_perimeter(self):
        return 3 * self.side1

    def compute_inner_angles(self):
        return [60, 60, 60]


class Isosceles(Triangle):
    def __init__(self, base=0, height=0, side=0):
        super().__init__(base=base, height=height, side1=base, side2=side, side3=side)
        self.is_regular = False



class TriRectangle(Triangle):
    def __init__(self, base=0, height=0, hypotenuse=0):
        super().__init__(base=base, height=height, side1=base, side2=height, side3=hypotenuse)
        self.is_regular = False

    def compute_inner_angles(self):
        angle_A = math.degrees(math.atan(self.height / self.base))
        angle_B = 90 - angle_A
        return [90, angle_A, angle_B]
    
```
***
### Ejemplo de uso

El ejemplo de uso crea 4 distintas formas geometricas (Triangulo escaleno, triangulo isoceles, triangulo rectangulo y cuadrado) y muestra la informacion de cada forma: base, altura, lados, area, perimetro, vertices, aristas y angulos internos

``` bash
# Creación de formas geometricas con sus medidas definidas
scalene = Scalene(base=3, height=4, side1=3, side2=4, side3=5)
square = Square(side=4)
isosceles = Isosceles(base=3, height=4, side=5)
triangle = TriRectangle(base=3, height=4, hypotenuse=5)

# Impresión de la informacion de cada forma geometrica
print(scalene.__str__())
print()

print(square.__str__())
print()

print(isosceles.__str__())
print()

print(triangle.__str__())

```
***
### Salida Esperada
``` bash
# Información del triángulo escaleno
Triangle:
  Base: 3
  Height: 4
  Side1: 3
  Side2: 4
  Side3: 5
  Area: 6.0
  Perimeter: 12
  Vertices: (0, 0), (3, 0), (1.5, 4)
  Edges: (0, 0) -> (3, 0), (3, 0) -> (1.5, 4), (1.5, 4) -> (0, 0)
  Inner Angles: 90.00, 36.87, 53.13

# Información del cuadrado
Square:
  Side: 4
  Area: 16
  Perimeter: 16
  Vertices: (0, 0), (4, 0), (4, 4), (0, 4)
  Edges: (0, 0) -> (4, 0), (4, 0) -> (4, 4), (4, 4) -> (0, 4), (0, 4) -> (0, 0)
  Inner Angles: 90.00, 90.00, 90.00, 90.00

# Información del triángulo isósceles
Triangle:
  Base: 3
  Height: 4
  Side1: 3
  Side2: 5
  Side3: 5
  Area: 6.0
  Perimeter: 13
  Vertices: (0, 0), (3, 0), (1.5, 4)
  Edges: (0, 0) -> (3, 0), (3, 0) -> (1.5, 4), (1.5, 4) -> (0, 0)
  Inner Angles: 36.87, 36.87, 106.26

# Información del triángulo rectángulo
Triangle:
  Base: 3
  Height: 4
  Side1: 3
  Side2: 4
  Side3: 5
  Area: 6.0
  Perimeter: 12
  Vertices: (0, 0), (3, 0), (1.5, 4)
  Edges: (0, 0) -> (3, 0), (3, 0) -> (1.5, 4), (1.5, 4) -> (0, 0)
  Inner Angles: 90.00, 53.13, 36.87

```

# RESTAURANTE


El código implementa un sistema de gestión de menús y órdenes para un restaurante utilizando herencia, encapsulamiento y polimorfismo. Define una clase base MenuItem con atributos comunes como el nombre y el precio, y clases derivadas (Beverage, Appetizer y MainCourse) que añaden características específicas como tamaño, ingredientes, y tipo. La clase Order permite agregar o eliminar platos y calcular el precio total, aplicando un descuento a las bebidas si la orden incluye un plato principal. Además, la clase Payment gestiona el procesamiento de pagos, asociando un método de pago con una orden. Este diseño modular permite organizar y gestionar fácilmente un menú, procesar órdenes y aplicar reglas comerciales específicas, como descuentos.
``` python
class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value


class Beverage(MenuItem):
    def __init__(self, name, price, size, is_cold, has_ice):
        super().__init__(name, price)
        self._size = size
        self._is_cold = is_cold
        self._has_ice = has_ice

    def get_size(self):
        return self._size

    def set_size(self, value):
        self._size = value

    def get_is_cold(self):
        return self._is_cold

    def set_is_cold(self, value):
        self._is_cold = value

    def get_has_ice(self):
        return self._has_ice

    def set_has_ice(self, value):
        self._has_ice = value

    def __str__(self):
        return (
            f"{self.get_name()} (Price: {self.get_price()}, Size: {self.get_size()}, "
            f"Cold: {self.get_is_cold()}, Ice: {self.get_has_ice()})"
        )


class Appetizer(MenuItem):
    def __init__(self, name, price, appetizer_type):
        super().__init__(name, price)
        self._appetizer_type = appetizer_type

    def get_appetizer_type(self):
        return self._appetizer_type

    def set_appetizer_type(self, value):
        self._appetizer_type = value

    def __str__(self):
        return f"{self.get_name()} (Price: {self.get_price()}, Type: {self.get_appetizer_type()})"


class MainCourse(MenuItem):
    def __init__(self, name, price, ingredients, salad):
        super().__init__(name, price)
        self._ingredients = ingredients
        self._salad = salad

    def get_ingredients(self):
        return self._ingredients

    def set_ingredients(self, value):
        self._ingredients = value

    def get_salad(self):
        return self._salad

    def set_salad(self, value):
        self._salad = value

    def __str__(self):
        return (
            f"{self.get_name()} (Price: {self.get_price()}, Ingredients: {self.get_ingredients()}, "
            f"Salad: {self.get_salad()})"
        )


class Order:
    def __init__(self):
        self.plates = []

    def add_plate(self, plate):
        self.plates.append(plate)

    def remove_plate(self, plate):
        self.plates.remove(plate)

    def total(self):
        return self.calculate_total_price()

    def calculate_total_price(self):
        total = sum(plate.get_price() for plate in self.plates)
        has_main_course = any(isinstance(plate, MainCourse) for plate in self.plates)
        if has_main_course:
            discount = sum(
                plate.get_price() * 0.1 for plate in self.plates if isinstance(plate, Beverage)
            )
            total -= discount
        return total

    def get_plate_details(self):
        return [str(plate) for plate in self.plates]

    def __str__(self):
        plate_details = "\n".join(self.get_plate_details())
        return f"Order:\n{plate_details}\nTotal: {self.total()}"


class Payment:
    def __init__(self, order, payment_method):
        self._order = order
        self._payment_method = payment_method

    def get_order(self):
        return self._order

    def set_order(self, value):
        self._order = value

    def get_payment_method(self):
        return self._payment_method

    def set_payment_method(self, value):
        self._payment_method = value

    def process_payment(self):
        print(
            f"Processing payment of {self._order.total()} using {self._payment_method}..."
        )
        print("Payment successful!")
```
***
### Ejemplo de uso

El ejemplo de uso crea tres elementos del menú (una bebida, un aperitivo y un plato principal), los agrega a una orden, muestra los detalles de la orden con el total calculado (incluyendo descuentos si aplican) y luego procesa el pago utilizando una tarjeta de crédito.

``` bash
coca_cola = Beverage("Coca Cola", 2000, "Large", True, True)
nachos = Appetizer("Nachos", 12000, "Shared")
spaghetti = MainCourse("Spaghetti", 25000, "Pasta and tomato sauce", False)

order = Order()
order.add_plate(coca_cola)
order.add_plate(nachos)
order.add_plate(spaghetti)

print(order)

payment = Payment(order, "Credit Card")
payment.process_payment()
```
***
### Salida Esperada
``` bash
Order:
Coca Cola (Price: 2000, Size: Large, Cold: True, Ice: True)
Nachos (Price: 12000, Type: Shared)
Spaghetti (Price: 25000, Ingredients: Pasta and tomato sauce, Salad: False)
Total: 37000
Processing payment of 37000 using Credit Card...
Payment successful!
```
