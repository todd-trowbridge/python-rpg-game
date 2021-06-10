from Character import Character

class Zombie(Character):
  def __init__(self):
    self.health = 0
    self.power = 1

  def is_alive(self):
    return True

  def print_status(self):
    print(f'The zombie has {self.health} health and {self.power} power.')