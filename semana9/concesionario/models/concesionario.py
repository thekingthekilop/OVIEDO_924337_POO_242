class Dealership:
    def __init__(self, name: str):
        self.__name = name
        self.__available_cars = []

    # Method to add a car to the list of available cars
    def add_car(self, car: Car):
        self.__available_cars.append(car)

    # Method to show all available cars
    def show_cars(self):
        if not self.__available_cars:
            return "No cars available."
        return "\n".join(str(car) for car in self.__available_cars)

    # Method to sell a car to a client
    def sell_car(self, client: Client, car: Car):
        if car in self.__available_cars:
            self.__available_cars.remove(car)
            client.buy_car(car)  # Assign the car to the client
            return f"The car {car.get_brand()} {car.get_model()} has been sold to {client.get_name()}."
        else:
            return "Car not available."