"""
Create by Killer at 2019-05-16 10:00
"""

import random

class Creature:

    def __init__(self, name, level):
        self._name = name
        self._level = level

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self._level


class Dragon(Creature):

    def __init__(self, name, level, scalines, breaths_fire):
        super().__init__(name, level)
        self._scalines = scalines
        self.breaths_fire = breaths_fire


    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self._scalines
        if self.breaths_fire:
            value = value * 2

        return value


class Wizard(Creature):

    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return my_roll >= their_roll