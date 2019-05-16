"""
Create by Killer at 2019-05-16 10:04
"""
from actors import Creature, Wizard, Dragon

import random

def main():
    print_header()
    game_loop()


def print_header():
    print('-------------------------------------')
    print('             WIZARD GAME')
    print('-------------------------------------')
    print()

def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scalines=2, breaths_fire=False),
        Wizard('Evil wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)

        print(f'A {active_creature._name} of level {active_creature._level} has appear from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?\n')

        if cmd=='a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print('The wizard defeated {}'.format(active_creature._name))
            else:
                print("The wizard has been defeat by the powerful {}".format(active_creature._name))
        elif cmd=='r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd=='l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero._name))
            for c in creatures:
                print(" * {} of level {}".format(c._name, c._level))
        else:
            print("Ok, exiting game.. bye!")
            break
        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == '__main__':
    main()