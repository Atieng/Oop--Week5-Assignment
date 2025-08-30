 
# Question 1: Design Your Own Class
 

class Smartphone:
    def __init__(self, brand, model, battery=100):
        # Encapsulation: battery is private
        self.brand = brand
        self.model = model
        self.__battery = battery  

    def make_call(self, number):
        if self.__battery > 10:
            self.__battery -= 10
            print(f"{self.brand} {self.model} is calling {number}")
        else:
            print("Battery too low to make a call  ")

    def charge(self):
        self.__battery = 100
        print(f"{self.brand} {self.model} is now fully charged")

    def check_battery(self):
        print(f"Battery level: {self.__battery}%")
        return self.__battery


# Inheritance + Polymorphism
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery=100, gpu="Adreno"):
        super().__init__(brand, model, battery)
        self.gpu = gpu

    # Overriding method (Polymorphism)
    def make_call(self, number):
        print(f"{self.brand} {self.model} (Gaming Edition 🎮) makes a high-speed VoIP call to {number}")


# ==============================
# Question 2: Polymorphism Challenge
# ==============================

class Animal:
    def move(self):
        print("Animals move in different ways.")

class Dog(Animal):
    def move(self):
        print("Dog is running")

class Bird(Animal):
    def move(self):
        print("Bird is flying")

class Vehicle:
    def move(self):
        print("Vehicles move differently.")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying")


 
if __name__ == "__main__":
    # Activity 1 demo
    phone1 = Smartphone("Samsung", "S22")
    phone1.make_call("123456789")
    phone1.check_battery()
    phone1.charge()

    gaming_phone = GamingPhone("Asus", "ROG Phone 7")
    gaming_phone.make_call("987654321")

    print("\n--- Activity 2: Polymorphism Demo ---")
    animals = [Dog(), Bird()]
    vehicles = [Car(), Plane()]

    for a in animals:
        a.move()

    for v in vehicles:
        v.move()
