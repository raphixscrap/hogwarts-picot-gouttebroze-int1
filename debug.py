import universe.house as house
import universe.character as character
from datetime import datetime

#TODO: REMOVE THIS FROM PRODUCTION

print("[DEBUG] - ONLY - NOT MEANT FOR PRODUCTION - (IF YOU SEE THIS .... NOT SUPPOSED TO)")
print("TIME : ", datetime.now())
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
    ),
    (
        "A troll has entered the dungeon! What is your immediate reaction?",
        ["Run towards it to fight", "Use the confusion to your advantage", "Ensure everyone gets to safety", "Research the troll's weaknesses"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "Which of these scents appeals to you the most?",
        ["A crackling log fire", "The salty sea breeze", "Freshly baked bread", "Old parchment and ink"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "You catch a classmate cheating on an exam. You...",
        ["Confront them loudly after class", "Blackmail them for a favor later", "Encourage them to study with you next time", "Inform the professor privately"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "What is your worst nightmare?",
        ["Being called a coward", "Being ignored or powerless", "Disappointing your friends", "Making a foolish mistake"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "Which path would you take in a magical forest?",
        ["The twisting, dark path", "The wide, sunlit path", "The path through the flower fields", "The path leading to an ancient ruin"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "It's Saturday night. Where are you?",
        ["Exploring the Forbidden Forest", "Networking with influential students", "In the common room with snacks", "In the library studying"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    )
]

harry = character.init_character("Potter", "Harry", {"Courage": 3, "Ambition":2, "Loyalty": 1, "Intelligence": 0})
print("UNIT TEST - ASSIGN HOUSE")
print(house.assign_house(harry, questions))
