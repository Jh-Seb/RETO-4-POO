class MenuItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

class Beverage(MenuItem):
    def __init__(self, name, price, size, is_cold, has_ice):
        super().__init__(name, price)
        self.__size = size
        self.__is_cold = is_cold
        self.__has_ice = has_ice

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_is_cold(self):
        return self.__is_cold

    def set_is_cold(self, is_cold):
        self.__is_cold = is_cold

    def get_has_ice(self):
        return self.__has_ice

    def set_has_ice(self, has_ice):
        self.__has_ice = has_ice

    def __str__(self):
        return "{} (Price: {}, Size: {}, Cold: {}, Ice: {})".format(
            self.get_name(), self.get_price(), self.__size, self.__is_cold, self.__has_ice
        )

class Appetizer(MenuItem):
    def __init__(self, name, price, appetizer_type):
        super().__init__(name, price)
        self.__appetizer_type = appetizer_type

    def get_appetizer_type(self):
        return self.__appetizer_type

    def set_appetizer_type(self, appetizer_type):
        self.__appetizer_type = appetizer_type

    def __str__(self):
        return "{} (Price: {}, Type: {})".format(
            self.get_name(), self.get_price(), self.__appetizer_type
        )

class MainCourse(MenuItem):
    def __init__(self, name, price, ingredients, salad):
        super().__init__(name, price)
        self.__ingredients = ingredients
        self.__salad = salad

    def get_ingredients(self):
        return self.__ingredients

    def set_ingredients(self, ingredients):
        self.__ingredients = ingredients

    def get_salad(self):
        return self.__salad

    def set_salad(self, salad):
        self.__salad = salad

    def __str__(self):
        return "{} (Price: {}, Ingredients: {}, Salad: {})".format(
            self.get_name(), self.get_price(), self.__ingredients, self.__salad
        )

class Order:
    def __init__(self):
        self.__plates = []  # Lista de platos

    def add_plate(self, plate):
        self.__plates.append(plate)

    def remove_plate(self, plate):
        try:
            self.__plates.remove(plate)
        except ValueError as e:
            print("Error al eliminar el plato:", e)

    def calculate_total_price(self):
        total = sum(plate.get_price() for plate in self.__plates)
        has_main_course = any(isinstance(plate, MainCourse) for plate in self.__plates)
        if has_main_course:
            discount = sum(plate.get_price() * 0.1 for plate in self.__plates if isinstance(plate, Beverage))
            total -= discount
        return total

    def get_plate_details(self):
        return [str(plate) for plate in self.__plates]

    def total(self):
        return self.calculate_total_price()

    def __str__(self):
        details = "\n".join(self.get_plate_details())
        return "Order:\n" + details + "\nTotal: " + str(self.calculate_total_price())

class Payment:
    def __init__(self, order, payment_method):
        self.order = order
        self.payment_method = payment_method

    def process_payment(self):
        print("Processing payment of {} using {}...".format(self.order.total(), self.payment_method))
        print("Payment successful!")

# Test del sistema
order = Order()
order.add_plate(MainCourse("Spaghetti", 25000, "Pasta and tomato sauce", False))
order.add_plate(Beverage("Coca Cola", 2000, "Large", True, True))

print(order)

payment = Payment(order, "Credit Card")
payment.process_payment()
