class Car:
   def __init__(self, brand, model):
       self.brand = brand
       self.model = model
       self.doors = 4

   def print_car(self):
       print(f"I am a {self.brand} {self.model}.")


class Pickup(Car):
   def __init__(self, brand, model):
       super().__init__(brand, model) #first use of super()
       self.doors = 2

   def print_pickup(self):
       self.print_car() #note what self contains here.
       print(f"I am a pickup truck and I have {self.doors} doors.")


def main():
   f250 = Pickup("Ford", "F-250")
   f250.print_pickup()


if __name__ == '__main__':
   main()
