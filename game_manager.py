import random
import math

import numpy
import numpy as np


class GameState:
    def __init__(self, name=None, experience=0, satiety=100, hygiene=100, drowsiness=100, hp=100):

        self.gameover = False
        self.experience = experience
        self.xp_per_level = 100
        self.satiety = satiety
        self.hygiene = hygiene
        self.drowsiness = drowsiness
        self.hp = hp
        self.base_difficulty_factor = 0.055
        self.max_difficulty_factor = 0.0358
        self.difficulty_factor = self.base_difficulty_factor

        self.start_interval = 1000
        self.end_interval = 100

        self.name = name

        # start hyperparameters

        self.base_eat_xp = 4

        self.start_hp_loss = 30
        self.max_hp_loss_pertick = 5
        self.expected_levels = 50

        self.tick_length = 1
        self.food_cooldown_ticks = 10

        self.eat_integral = []
        self.current_tick = 0

        self.gameOver()


    def get_tick(self):
        level = math.floor(self.experience / self.xp_per_level)
        return int((self.start_interval - self.end_interval)/(-self.expected_levels) * level + self.start_interval)

    def increment_xp(self, amount):
        start_level = math.floor(self.experience / self.xp_per_level)
        self.experience += amount
        self.experience = max(0, self.experience)
        end_level = math.floor(self.experience / self.xp_per_level)
        self.hp += (end_level - start_level) * 10
        self.hp = min(100, self.hp)

    def eat(self):
        if len(self.eat_integral) == 0:
            return
        satiety_vals = np.array(self.eat_integral)
        self.satiety += np.sum(self.eat_gain_func(satiety_vals, self.difficulty_factor))
        self.satiety = min(100, max(0, self.satiety))
        self.experience += self.base_eat_xp + random.randrange(-self.base_eat_xp, self.base_eat_xp) + len(self.eat_integral)
        experience_bonus = 0 if len(self.eat_integral) >= 10 else self.base_eat_xp + random.randrange(-self.base_eat_xp, self.base_eat_xp)
        self.increment_xp(int(len(self.eat_integral)/3) + experience_bonus)
        self.eat_integral = []

    def satiety_loss_func(self, x):
        return 24 - 12 * np.log10(x) + 0.1

    def drowsiness_loss_func(self, x):
        return 30 - 15 * np.log10(x) + 0.1

    def eat_gain_func(self, x, difficulty):
        return (difficulty * (x - 100)) ** 2

    def satiety_loss(self):
        if self.satiety <= 0:
            self.satiety = 0
            return
        self.satiety -= self.satiety_loss_func(self.satiety)
        self.satiety = min(100, max(0, self.satiety))

    def sleep(self):
        self.increment_xp(int((100 - self.drowsiness) / 4))
        self.drowsiness = 100

    def wash(self):
        self.increment_xp(int((100 - self.hygiene) / 4))
        self.hygiene = 100

    def drowsiness_loss(self):
        if self.drowsiness <= 0:
            self.drowsiness = 0
            return
        self.drowsiness -= self.drowsiness_loss_func(self.drowsiness)
        self.drowsiness = min(100, max(0, self.drowsiness))

    def hygiene_loss(self):
        if self.hygiene <= 0:
            self.hygiene = 0
            return
        self.hygiene -= 1

    def hp_loss_func(self, x):

        def loss_func(_x):
            if _x <= self.start_hp_loss:
                self.current_hp_loss = (self.max_hp_loss_pertick - 0.5) / self.expected_levels * int(self.expected_levels / 100)
                return (0.5 - self.current_hp_loss)/30 * _x + self.max_hp_loss_pertick
            else:
                return 0

        if isinstance(x, np.ndarray):
            return np.vectorize(loss_func)(x)
        else:
            return loss_func(x)

    def tick(self):
        start_level = math.floor(self.experience / self.xp_per_level)
        self.difficulty_factor = self.base_difficulty_factor + int(self.experience / self.xp_per_level) * (self.base_difficulty_factor - self.max_difficulty_factor) / -self.expected_levels
        self.satiety_loss()
        self.hygiene_loss()
        if self.satiety > 0:
            self.eat_integral.append(self.satiety)
        self.drowsiness_loss()
        worst_metric = min(self.satiety, self.drowsiness)
        self.hp -= self.hp_loss_func(worst_metric)
        self.hp = max(0, self.hp)
        end_level = math.floor(self.experience / self.xp_per_level)
        self.hp += (end_level - start_level) * 10
        self.hp = min(100, self.hp)

    def gameOver(self):
        if self.hp == 0:
            self.gameover = True
        else:
            self.gameover = False
        return self.gameover

