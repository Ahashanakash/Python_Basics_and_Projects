from person import Person
import random

class Teachers(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
    def evaluate_exam(self):
        return random.randint(50, 100)