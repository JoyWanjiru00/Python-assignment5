# 📘 Assignment 1 & Activity 2 - Python OOP

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python, including **classes, constructors, inheritance, and polymorphism**.

---

## 🚀 Assignment 1: Design Your Own Class

We created a `Smartphone` class with attributes and methods that bring it to life. A subclass `GamingPhone` is also added to demonstrate inheritance and method overriding.

### Features

* **Smartphone Class**

  * Attributes: `brand`, `model`, `battery`, `apps`
  * Methods:

    * `make_call(number)`: Simulates making a phone call.
    * `charge(amount)`: Charges the battery up to 100%.
    * `install_app(app)`: Installs a new app.

* **GamingPhone Class** *(inherits from Smartphone)*

  * Additional attribute: `cooling_system`
  * Additional method:

    * `play_game(game)`: Plays a game and consumes more battery.

### Example Usage

```python
phone1 = Smartphone("Apple", "iPhone 14", 80)
phone1.make_call("123-456-7890")
phone1.install_app("WhatsApp")
phone1.charge(15)

gaming_phone = GamingPhone("Asus", "ROG 6", 60, "liquid")
gaming_phone.play_game("PUBG")
gaming_phone.install_app("Discord")
```

---

## 🎭 Activity 2: Polymorphism Challenge

We created a `Vehicle` base class with subclasses that implement their own `move()` methods differently.

### Classes

* `Car` → `move()` prints **"Driving 🚗"**
* `Plane` → `move()` prints **"Flying ✈️"**
* `Boat` → `move()` prints **"Sailing 🚤"**

### Example Usage

```python
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
```

### Output

```
Driving 🚗
Flying ✈️
Sailing 🚤
```

---

## 🧩 Concepts Demonstrated

* **Classes & Objects**
* **Constructors (`__init__`)**
* **Encapsulation** (through methods & attributes)
* **Inheritance** (Smartphone → GamingPhone)
* **Polymorphism** (different `move()` implementations)

---

## 🛠️ How to Run

1. Clone or download the project.
2. Run the Python file:

   ```bash
   python class_and_polymorphism.py
   ```

---

## 📌 Next Steps

* Add more `Vehicle` subclasses (Bike, Train, Rocket 🚀).
* Write **unit tests** to validate behavior.
* Extend `Smartphone` with more real-life features.
