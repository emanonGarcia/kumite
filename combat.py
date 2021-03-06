import random


class Combat:

    dodge_limit = 6
    attack_limit = 6

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 4

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4

    def get_user_input(self, msg):
        user_input = ''
        while not user_input and len(user_input) > 0:
            user_input = input(msg)
        return user_input.lower()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
