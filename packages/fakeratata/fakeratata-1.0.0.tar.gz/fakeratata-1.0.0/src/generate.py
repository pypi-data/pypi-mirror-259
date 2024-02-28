import random

class FakeNameGenerator:
    def __init__(self):
        self.first_names = [
            "John", "Jane", "David", "Sarah", "Michael", "Emily", "Daniel",
            "Olivia", "Matthew", "Sophia", "Andrew", "Ava", "William", "Mia",
            "Joseph", "Isabella", "James", "Charlotte", "Christopher", "Amelia"
        ]
        self.last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis",
            "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas",
            "Hernandez", "Moore", "Walker", "Perez", "Hall", "Young"
        ]

    def generate_name(self):
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return f"{first_name} {last_name}"

    def generate_package(self, num_names):
        package = []
        for _ in range(num_names):
            name = self.generate_name()
            package.append(name)
        return package

