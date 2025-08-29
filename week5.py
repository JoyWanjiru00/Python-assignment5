# Assignment 1: Design Your Own Class
class Smartphone:
    def __init__(self, brand: str, model: str, battery: int):
        self.brand = brand
        self.model = model
        self.battery = battery  # battery percentage
        self.apps = []

    def make_call(self, number: str):
        if self.battery > 0:
            print(f"{self.brand} {self.model} is calling {number}...")
            self.battery -= 5
        else:
            print("Battery too low to make a call!")

    def charge(self, amount: int):
        self.battery = min(100, self.battery + amount)
        print(f"Charged to {self.battery}%")

    def install_app(self, app: str):
        self.apps.append(app)
        print(f"{app} installed on {self.brand} {self.model}.")


class GamingPhone(Smartphone):
    def __init__(self, brand: str, model: str, battery: int, cooling_system: str):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game: str):
        if self.battery > 10:
            print(f"Playing {game} with {self.cooling_system} cooling system!")
            self.battery -= 15
        else:
            print("Battery too low to play games!")


# Example usage
phone1 = Smartphone("Apple", "iPhone 14", 80)
phone1.make_call("123-456-7890")
phone1.install_app("WhatsApp")
phone1.charge(15)


gaming_phone = GamingPhone("Asus", "ROG 6", 60, "liquid")
gaming_phone.play_game("PUBG")
gaming_phone.install_app("Discord")


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move() method")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
