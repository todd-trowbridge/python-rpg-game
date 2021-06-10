class Character:
  def __init__(self):
    self.health = 1
    self.power = 1

  def attack(self, character):
    character.health -= self.power

  def is_alive(self):
    if self.health > 0: return True
    else: return False

  def print_status(self):
    print(f'health: {self.health}\npower: {self.power}')