import hogwarts.universe.house as house
import hogwarts.universe.character as character
import hogwarts.chapters.chapter_1 as chapter1
from hogwarts.chapters.chapter_1 import start_chapter_1
from hogwarts.chapters.chapter_2 import start_chapter_2, enter_common_room
from hogwarts.chapters.chapter_3 import start_chapter_3
from hogwarts.chapters.chapter_4 import *
from hogwarts.utils.input_utils import load_file

#TODO: REMOVE THIS FROM PRODUCTION
questions = [
    (
        "Which subject at Hogwarts interests you the most?",
        ["Defense Against the Dark Arts", "Potions", "Herbology", "History of Magic"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "You find a locked door in a mysterious corridor. What do you do?",
        ["Try to break it down", "Pick the lock quietly", "Knock and ask if anyone is there", "Look for a key or solve the riddle"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "How would you like to be remembered in history?",
        ["As a bold hero", "As a powerful ruler", "As a kind soul", "As a wise genius"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "If you could have one superpower, what would it be?",
        ["Super strength", "Invisibility", "Talking to animals", "Mind reading"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    )
]
harry = character.init_character("Pottebeur", "Harry", {"Courage": 3, "Ambition":2, "Loyalty": 1, "Intelligence": 0})
harry["House"] = "Gryffindor"
houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }
#print(house.assign_house(harry, questions))
#ron = chapter1.create_character()
#enter_common_room(harry)
#start_chapter_1()
#start_chapter_2(harry)
#start_chapter_3(harry,houses)
teams_data = load_file("hogwarts/data/teams_quidditch.json")
attack = create_team('Slytherin', teams_data["Slytherin"])
defense = create_team('Gryffindor', teams_data["Gryffindor"], True, harry)

quidditch_match(harry, houses)