class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price
    
    def display_info(self):
        print(f"Smartphone Info:\nBrand: {self.brand}\nModel: {self.model}\nStorage: {self.storage} GB\nPrice: ${self.price}")
    
    def call(self, number):
        print(f"Calling {number}...")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, price, battery_life):
        super().__init__(brand, model, storage, price)
        self.battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"Battery Life: {self.battery_life} hours")

    def play_game(self, game):
        print(f"Playing {game} on {self.model}...")

# Testing the class
smartphone = Smartphone("Apple", "iPhone 13", 128, 799)
smartphone.display_info()
smartphone.call("123-456-7890")

gaming_phone = GamingSmartphone("Razer", "Razer Phone 2", 512, 999, 10)
gaming_phone.display_info()
gaming_phone.play_game("PUBG Mobile")
