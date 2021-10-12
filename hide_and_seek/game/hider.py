import random

class Hider:

    def __init__(self):

        self.location = random.randint(1, 1000)
        self.distance = [0, 0]

    def get_hint(self):

        hint = "(^_^) Hello there!"
        if self.distance[-1] > self.distance[-2]:
            hint = "(^.^) Getting colder!"
        if self.distance[-1] < self.distance[-2]:
            hint = "(>.<) Getting warmer!"
        if self.distance[-1] == 0:
            hint = "(;.;) You found me!"
        return hint

    def watch(self, location):

        distance = abs(self.location - location)
        self.distance.append(distance)

    # TODO: Define the Hider class here