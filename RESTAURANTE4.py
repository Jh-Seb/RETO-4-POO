class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class Beverage(MenuItem):
    def __init__(self, name, price, size, is_cold, has_ice):
        super().__init__(name, price)
        self._size = size
        self._is_cold = is_cold
        self._has_ice = has_ice

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def is_cold(self):
        return self._is_cold

    @is_cold.setter
    def is_cold(self, value):
        self._is_cold = value

    @property
    def has_ice(self):
        return self._has_ice

    @has_ice.setter
    def has_ice(self, value):
        self._has_ice = value

    def __str__(self):
        return (
            f"{self.name} (Price: {self.price}, Size: {self.size}, "
            f"Cold: {self.is_cold}, Ice: {self.has_ice})"
        )


class Appetizer(MenuItem):
    def __init__(self, name, price, appetizer_type):
        super().__init__(name, price)
        self._appetizer_type = appetizer_type

    @property
    def appetizer_type(self):
        return self._appetizer_type

    @appetizer_type.setter
    def appetizer_type(self, value):
        self._appetizer_type = value

    def __str__(self):
        return f"{self.name} (Price: {self.price}, Type: {self.appetizer_type})"


class MainCourse(MenuItem):
    def __init__(self, name, price, ingredients, salad):
        super().__init__(name, price)
        self._ingredients = ingredients
        self._salad = salad

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = value

    @property
    def salad(self):
        return self._salad

    @salad.setter
    def salad(self, value):
        self._salad = value

    def __str__(self):
        return (
            f"{self.name} (Price: {self.price}, Ingredients: {self.ingredients}, "
            f"Salad: {self.salad})"
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
        total = sum(plate.price for plate in self.plates)
        has_main_course = any(isinstance(plate, MainCourse) for plate in self.plates)
        if has_main_course:
            discount = sum(
                plate.price * 0.1 for plate in self.plates if isinstance(plate, Beverage)
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
        self.order = order
        self.payment_method = payment_method

    def process_payment(self):
        print(
            f"Processing payment of {self.order.total()} using {self.payment_method}..."
        )
        print("Payment successful!")


# Test del sistema
order = Order()
order.add_plate(MainCourse("Spaghetti", 25000, "Pasta and tomato sauce", False))
order.add_plate(Beverage("Coca Cola", 2000, "Large", True, True))

print(order)

payment = Payment(order, "Credit Card")
payment.process_payment()
