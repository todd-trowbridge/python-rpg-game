from random import randrange

class Character:
  def __init__(self):
    self.health = 1
    self.max_power = 1
    self.power = 1

  def attack(self, character):
    character.health -= self.power

  def is_alive(self):
    if self.health > 0: return True
    else: return False

  def print_status(self):
    print(f'health: {self.health}\npower: {self.power}'.upper())

  def set_power(self):
    self.power = randrange(0,self.max_power+1)