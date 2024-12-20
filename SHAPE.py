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
    


# Ejemplo de uso
scalene = Scalene(base=3, height=4, side1=3, side2=4, side3=5)
square = Square(side=4)
isosceles = Isosceles(base=3, height=4, side=5)
print(square.__str__())