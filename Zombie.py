from Character import Character
from random import randrange

class Zombie(Character):
  def __init__(self):
    self.health = 'undead'
    self.max_power = 10
    self.power = 10

  def is_alive(self):
    return True

  def print_status(self):
    print(f'The zombie has {self.health} health and {self.power} power.'.upper())