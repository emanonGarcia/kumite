import random
from combat import Combat


class Character(Combat):
    experience = 0
    base_hit_points = 10
    attack_limit = 10

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.fighting_style = self.get_fighting_style()
        self.hit_points = self.base_hit_points
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}: {} figher HP: {}, EXP: {}".format(
            self.name,
            self.fighting_style,
            self.hit_points,
            self.experience)

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.fighting_style == 'Kung-fu':
            roll += 1
        elif self.fighting_style == 'Jiu-jitsu':
            roll += 2
        elif self.fighting_style == 'Muay Thai':
            roll += 3
        return roll > 4

    def get_fighting_style(self):
        style_choice = input("Pick your style: [K]ung-fu, [M]uay Thai, or [J]iu-jitsu: ").lower()

        if style_choice == 'k' or style_choice[0] == 'k':
            return "Kung-fu"
        elif style_choice == 'm' or style_choice[0] == 'm':
            return "Muay Thai"
        elif style_choice == 'j' or style_choice[0] == 'j':
            return "Jiu-jitsu"
        else:
            self.get_fighting_style()

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def leveled_up(self):
        return self.experience >= 5

    def got_hit(self):
        self.hit_points -= 1
