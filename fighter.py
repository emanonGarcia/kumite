import random
from combat import Combat


class Fighter(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1

    def __init__(self, **kwargs):

        self.hit_points = random.randint(self.min_hit_points,
                                         self.max_hit_points)
        self.experience = random.randint(self.min_experience,
                                         self.max_experience)
        self.name = self.__class__.__name__
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}: {} fighter, HP = {}, XP = {}".format(
            self.name,
            self.fighting_style,
            self.hit_points,
            self.experience)

    def battlecry(self):
        return self.sound.upper()


class Sagat(Fighter):
    fighting_style = 'Muay Thai'
    min_hit_points = 5
    min_experience = 6
    max_hit_points = 10
    max_experience = 10
    sound = "hahaha"

    def battlecry(self):
        return "HAAHA"


class Renato(Fighter):
    fighting_style = 'Jiu jitsu'
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = "hespect my gi"


class Monk(Fighter):
    fighting_style = 'Kung-fu'
    min_hit_points = 5
    max_hit_points = 8
    min_experience = 6
    max_experience = 10
    sound = "come try my wu-tang style"
