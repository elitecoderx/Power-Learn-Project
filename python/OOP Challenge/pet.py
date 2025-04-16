class Pet:
    def __init__(self, name, pet_type="🐾 Pet"):
        self.name = name
        self.type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍽️ {self.name} is eating... Hunger: {old_hunger} → {self.hunger}, Happiness +1")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"😴 {self.name} is sleeping... Energy: {old_energy} → {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎾 {self.name} is playing! Energy -2, Happiness +2, Hunger +1")
        else:
            print(f"⚠️ {self.name} is too tired to play. Let them rest! 😓")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"🎓 {self.name} learned a new trick: {trick}!")
        else:
            print(f"🧐 {self.name} already knows how to {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"🧠 {self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"🤷 {self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"\n📊 {self.name}'s Status Report 🐶")
        print(f"🔹 Type: {self.type}")
        print(f"🍗 Hunger   : {self.hunger}/10")
        print(f"⚡ Energy   : {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10")
        print(f"🎩 Tricks   : {', '.join(self.tricks) if self.tricks else 'None'}")
