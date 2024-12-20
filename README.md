# RETO-4-POO

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
