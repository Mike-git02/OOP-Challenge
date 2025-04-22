import time

class Pet:
    def __init__(self, name):
        """
        Initialize the pet with default values and a name.
        """
        self.name = name
        self.hunger = 5        # 0 = full, 10 = very hungry
        self.energy = 5        # 0 = tired, 10 = full energy
        self.happiness = 5     # 0 = sad, 10 = very happy
        self.tricks = []       # List to store learned tricks

    def eat(self):
        """
        Reduces hunger by 3 (not below 0), and increases happiness by 1 (not above 10).
        """
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        time.sleep(1)
        print(f"{self.name} has eaten. 🍽️")

    def sleep(self):
        """
        Increases energy by 5 points (not above 10).
        """
        self.energy = min(self.energy + 5, 10)
        time.sleep(1)
        print(f"{self.name} has slept. 💤")

    def play(self):
        """
        Pet plays: energy -2, happiness +2, hunger +1.
        Cannot play if energy is less than 2.
        """
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            time.sleep(1)
            print(f"You played with {self.name}. 🐾")
        else:
            print(f"{self.name} is too tired to play. 😴")

    def get_status(self):
        """
        Prints the pet's current status: hunger, energy, happiness, tricks.
        """
        print(f"\n📋 {self.name}'s Status:")
        print(f"🍗 Hunger: {self.hunger}")
        print(f"⚡ Energy: {self.energy}")
        print(f"😊 Happiness: {self.happiness}")
        print(f"🎓 Tricks: {', '.join(self.tricks) if self.tricks else f'{self.name} hasn\'t learned any tricks yet.'}")
        time.sleep(2)

    def train(self, trick):
        """
        Teaches the pet a new trick if not already known.
        """
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick}'. 😉")
        else:
            self.tricks.append(trick)
            time.sleep(1)
            print(f"{self.name} learned a new trick: '{trick}'! 🎉")

    def show_tricks(self):
        """
        Displays all tricks the pet has learned.
        """
        print(f"\n🎩 {self.name}'s Tricks:")
        if self.tricks:
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
