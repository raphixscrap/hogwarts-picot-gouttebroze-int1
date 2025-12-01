import hogwarts.universe.house as house
import hogwarts.universe.character as character

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
harry = character.init_character("Potter", "Harry", {"Courage": 3, "Ambition":2, "Loyalty": 1, "Intelligence": 0})
print(house.assign_house(harry, questions))
