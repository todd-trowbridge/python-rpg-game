from Character import Character
from random import randrange

class Goblin(Character):
  def __init__(self):
    self.health = 18
    self.max_power = 6
    self.power = 6

  def print_status(self):
    print(f'The goblin has {self.health} health and {self.power} power.'.upper())