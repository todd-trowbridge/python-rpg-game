from Hero import Hero
from Goblin import Goblin
from Zombie import Zombie
from Character import Character
from random import randrange

def fight(character1, character2):
  # stop the loop if the hero dies
  while hero.health > 0:
    # print character's health
    character1.print_status()
    character2.print_status()
    # battle_message defined below
    battle_choice = int(input(battle_message))
    if battle_choice == 1:
      if character1.is_alive() and character2.is_alive():
        character1.set_power()
        character1.attack(character2)
        character2.set_power()
        character2.attack(character1)
      if not character2.is_alive() and not character1.is_alive():
          print("Congrats, you both died.".upper())
          break
      elif not character2.is_alive():
        if isinstance(character2, Goblin):
          print("Congratulations, you've murdered a goblin".upper())
        break
      elif not character1.is_alive():
        print("You've been struck by, you've been killed by a smooth criminal".upper())
        break
    elif battle_choice == "2":
      pass
    elif battle_choice == "3":
      print("You ran away".upper())
      break

battle_message = f"""
(1) Attack
(2) Stare at the sky
(3) Run away
: """.upper()

welcome_message = """
-----Welcome to Fight Club-----

  (1) Fight a nearby goblin
  (2) Fight a nearby zombie
  (3) Talk about fight club
: """.upper()

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