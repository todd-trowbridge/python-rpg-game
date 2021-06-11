from Character import Character
from random import randrange

class Hero(Character):
  def __init__(self):
    self.health = 30
    self.max_power = 10
    self.power = 10

  def print_status(self):
    print(f'You have {self.health} health and {self.power} power.'.upper())