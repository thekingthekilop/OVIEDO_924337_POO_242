class Car:
    def __init__(self, brand: str, model: str, year: int, price: float):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand: str):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model: str):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year: int):
        self.__year = year

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price

    def __str__(self):
        return f"Car: {self.__brand} {self.__model}, Year: {self.__year}, Price: ${self.__price:.2f}"

    def apply_discount():
        pass
