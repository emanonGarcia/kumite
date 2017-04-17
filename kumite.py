import sys
from character import Character
from fighter import Monk
from fighter import Renato
from fighter import Sagat


class Kumite:

    def setup(self):
        self.player = Character()
        self.fighters = [
          Monk(),
          Renato(),
          Sagat()
        ]

        self.opponent = self.get_next_fighter()
        print('You will fight {}'.format(self.opponent))

    def get_next_fighter(self):
        try:
            return self.fighters.pop(0)
        except IndexError:
            return None

    def opponent_turn(self):

        if self.opponent.attack():
            print("{} is attacking!".format(self.opponent.name))
            self.dodge_response = input("Do you want to dodge? Y/n ").lower()
            if self.dodge_response == 'y' or self.dodge_response[0] == 'y':
                if self.player.dodge():
                    print("You dodged the attack")
                else:
                    print("You did not dodge successfully. {} hit you".format(self.opponent.name))
                    self.player.got_hit()
            else:
                print("{} hit you for 1 point".format(self.opponent.name))
                self.player.got_hit()
        else:
            print("{} did not attack this turn".format(self.opponent.name))

    def player_turn(self):
        self.player_response = input("Do you want to [A]ttack, [R]est, or say [M]atte: ").lower()
        if self.player_response == "a" or self.player_response[0] == "a":
            print("\nYou're attacking {}".format(self.opponent))
            if self.player.attack():
                if self.opponent.dodge():
                    print("** {} dodged your attack **".format(self.opponent.name))
                else:
                    print("** Your attack was successful! **")
                    if self.player.leveled_up():
                        self.opponent.hit_points -= 2
                    else:
                        self.opponent.hit_points -= 1
                    print("You hit {}!".format(self.opponent.name))
            else:
                print("** You missed! **")
        elif self.player_response == "r" or self.player_response[0] == "r":
            self.player.rest()
        elif self.player_response == "m" or self.player_response[0] == "m":
            print("Quitter!")
            sys.exit()
        else:
            self.player_turn()

    def cleanup(self):
        if self.opponent.hit_points <= 0:
            print("You killed {}".format(self.opponent.name))
            print("You get {} XP".format(self.opponent.experience))
            self.player.experience += self.opponent.experience
            self.opponent = self.get_next_fighter()

    def __init__(self):

        self.setup()

        while self.player.hit_points and (self.opponent or self.fighters):
            print("\n" + "="*20)
            print(self.player)
            self.opponent_turn()
            print("-"*20)
            self.player_turn()
            self.cleanup()
            print("\n" + "="*20)

        if self.player.hit_points:
            print("Victory! You are the grand champion")
        elif self.fighters or self.opponent:
            print("You lose! Death is your reward")
        sys.exit()

if __name__ == "__main__":
    print("Welcome to the Kumite. Test your might!")
    Kumite()
