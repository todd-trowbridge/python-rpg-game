from Hero import Hero
from Goblin import Goblin
from Zombie import Zombie

def fight(character1, character2):
  while hero.health > 0:
    character1.print_status()
    character2.print_status()
    battle_choice = int(input(battle_message))
    if battle_choice == 1:
      if character1.is_alive() and character2.is_alive():
        character2.attack(character1)
        character1.attack(character2)
      if not character2.is_alive() and not character1.is_alive():
          print("Congrats, you both died.")
          break
      elif not character2.is_alive():
        print('You killed them!')
        break
      elif not character1.is_alive():
        print("You've been struck by (and killed by) a smooth criminal")
        break
    elif battle_choice == "2":
      pass
    elif battle_choice == "3":
      print("You ran away")
      break

battle_message = f"""
(1) Attack
(3) Stare at the sky
(4) Run away
"""

welcome_message = """
Welcome to fight club.

(1) Fight a nearby goblin
(2) Fight a nearby zombie
(3) Talk about fight club.
"""

while True:
  goblin = Goblin()
  hero = Hero()
  zombie = Zombie()

  menu_choice = int(input(welcome_message))
  if menu_choice == 1:
    fight(hero, goblin)
  if menu_choice == 2:
    fight(hero, zombie)
  if menu_choice == 3:
    break