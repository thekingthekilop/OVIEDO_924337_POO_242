class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}"

    def __repr__(self):
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year})"

my_car = Car("Toyota", "Corolla", 2022)

print(str(my_car))
print(repr(my_car))


class BankAccount:
    def __init__(self, holder):
        self.holder = holder
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} completed successfully.")
        else:
            print("The deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} completed successfully.")
        else:
            print("Insufficient funds or invalid amount.")

    def show_balance(self):
        return f"The current balance is: {self.__balance}"

account = BankAccount("Carlos")
account.deposit(1000)
account.withdraw(500)

print(account.show_balance())
