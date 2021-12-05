import random
import math

import numpy as np


class GameState:
    def __init__(self, experience=0, satiety=100, hygiene=100, drowsiness=100, hp=100):
        self.experience = experience
        self.satiety = satiety
        self.hygiene = hygiene
        self.drowsiness = drowsiness
        self.hp = hp
        self.base_difficulty_factor = 0.055
        self.difficulty_factor = self.base_difficulty_factor

        # start hyperparameters

        self.base_eat_xp = 25

        self.start_hp_loss = 30
        self.max_hp_loss_pertick = 5
        self.expected_levels = 50

        self.tick_length = 1
        self.food_cooldown_ticks = 10

        self.eat_integral = []
        self.current_tick = 0

    def eat(self):
        satiety_vals = np.array(self.eat_integral)
        self.satiety += np.sum((self.difficulty_factor * (satiety_vals - 100)) ** 2)
        self.satiety = min(100, max(0, self.satiety))
        self.eat_integral = []
        self.experience += self.base_eat_xp + random.randrange(-7, 7)

    def satiety_loss(self):
        self.satiety -= 24 - 12 * math.log(self.satiety)
        self.satiety = min(100, max(0, self.satiety))

    def sleep(self):
        self.drowsiness = 100

    def drowsiness_loss(self):
        self.drowsiness -= 30 - 15 * math.log(self.drowsiness) + 1
        self.drowsiness = min(100, max(0, self.drowsiness))

    def calculate_hp_loss(self, x):
        if x <= self.start_hp_loss:
            self.current_hp_loss = (self.max_hp_loss_pertick - 0.5) / self.expected_levels * int(self.expected_levels / 100)
            return (0.5 - self.current_hp_loss)/30 * x + self.max_hp_loss_pertick
        else:
            return 0

    def tick(self):
        self.difficulty_factor = self.base_difficulty_factor - int(self.experience / 100) * (0.055 - 0.0358) / self.expected_levels
        self.satiety_loss()
        self.eat_integral.append(self.satiety)
        self.drowsiness_loss()
        worst_metric = min(self.satiety, self.drowsiness)
        self.hp -= self.calculate_hp_loss(worst_metric)

