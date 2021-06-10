from Character import Character

class Hero(Character):
  def __init__(self):
    self.health = 10
    self.power = 5

  def print_status(self):
    print(f'You have {self.health} health and {self.power} power.')