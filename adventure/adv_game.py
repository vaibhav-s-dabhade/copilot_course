clues = [
    "There is a faded photograph of a grand ball, the guests' faces blurred with time.",
    "There is a worn-out diary, its pages filled with tales of epic adventures.",
    "There is a shattered mirror, reflecting a room that doesn't quite match yours.",
    "There is a dusty old map, its edges frayed and locations unrecognizable.",
    "There is a cryptic inscription on the wall, its meaning lost to time.",
    "There is a single feather, its origin unknown, lying in the corner.",
    "There is a forgotten melody playing from an unseen source.",
    "There is a strange symbol etched into the floor, its purpose unclear.",
    "There is a peculiar scent in the air, reminiscent of a time long past.",
    "There is a mysterious light flickering intermittently from beneath the door."
]

sense_exp = [
    "You see a flickering candle casting long, dancing shadows on the stone walls.",
    "You hear the distant echo of footsteps, but can't tell where they're coming from.",
    "You smell the musty scent of old books and parchment.",
    "You touch the cold, rough stone of the wall, worn by centuries of history.",
    "You intuit a sense of foreboding, as if the castle itself is watching you.",
    "You see a tapestry, its colors faded, depicting a battle long past.",
    "You hear the soft rustling of a curtain in the breeze from a hidden window.",
    "You smell the faint aroma of a meal cooked hours, or perhaps days, ago.",
    "You touch a velvet drapery, its once vibrant color now dulled by dust and time.",
    "You intuit a presence in the room, though you see no one.",
    "You see a suit of armor, its metal tarnished and covered in cobwebs.",
    "You hear the distant tolling of a bell, its sound muffled and melancholic."
]

import random

class RandomItemSelector:
    def __init__(self, items):
        self.items = items
        self.used_items = []

    def add_item(self, item):
        self.items.append(item)

    def pull_random_item(self):
        if not self.items:
            return None
        if not set(self.items).difference(self.used_items):
            self.reset()
        item = random.choice(list(set(self.items).difference(self.used_items)))
        self.used_items.append(item)
        return item

    def reset(self):
        self.used_items = []


class SenseClueGenerator:
    _instance = None

    def __new__(cls, clues, sense_exp):
        if cls._instance is None:
            cls._instance = super(SenseClueGenerator, cls).__new__(cls)
            cls._instance.clue_selector = RandomItemSelector(clues)
            cls._instance.sense_selector = RandomItemSelector(sense_exp)
        return cls._instance

    def get_senseclue(self):
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"
   

from enum import Enum

class EncounterOutcome(Enum):
    CONTINUE = 1
    END = 2


from abc import ABC, abstractmethod

class Encounter(ABC):
    @abstractmethod
    def run_encounter(self):
        pass


class DefaultEncounter(Encounter):
    def __init__(self, clues, sense_exp):
        self.sense_clue_generator = SenseClueGenerator(clues, sense_exp)

    def run_encounter(self):
        sense_clue = self.sense_clue_generator.get_senseclue()
        print(sense_clue)
        return EncounterOutcome.CONTINUE
   

class Room:
    def __init__(self, name, encounter):
        self.name = name
        self.encounter = encounter

    def visit_room(self):
        return self.encounter.run_encounter()
   


# Define the room names
room_names = ["Throne Room", "Armory", "Library", "Dungeon", "Observatory", "Royal Chamber"]

# Create the rooms
rooms = [Room(name, DefaultEncounter(clues, sense_exp)) for name in room_names]


class Castle:
    def __init__(self, rooms):
        self.room_selector = RandomItemSelector(rooms)

    def select_door(self):
        door_count = random.randint(2, 4)
        print(f"There are {door_count} doors. Choose a door number between 1 and {door_count}.")

        while True:
            door_number = input("Your choice: ")
            if door_number.isdigit() and 1 <= int(door_number) <= door_count:
                return int(door_number)
            else:
                print(f"Invalid input. Please enter a number between 1 and {door_count}.")

    def next_room(self):
        self.select_door()
        room = self.room_selector.pull_random_item()
        print(f"You have entered the {room.name}.")
        return room.visit_room()

    def reset(self):
        self.room_selector.reset()


class Game:
    def __init__(self, rooms):
        self.castle = Castle(rooms)

    def play_game(self):
        print("Welcome to the Castle! Your objective is to navigate through the castle and find the treasure.")

        while True:
            outcome = self.castle.next_room()
            if outcome == EncounterOutcome.END:
                self.castle.reset()
                print("Game Over. You have found the treasure!")
                play_again = input("Would you like to explore a different castle? (yes/no): ")
                if play_again.lower() != "yes":
                    break


# run the game
game = Game(rooms)
game.play_game()
