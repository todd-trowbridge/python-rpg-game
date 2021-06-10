from Character import Character

class Goblin(Character):
  def __init__(self):
    self.health = 6
    self.power = 2

  def print_status(self):
    print(f'The goblin has {self.health} health and {self.power} power.')