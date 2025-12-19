from hogwarts.universe.character import display_character, add_item
from hogwarts.universe.house import update_house_points, display_winning_house
from hogwarts.utils.input_utils import print_bar, load_file, ask_text, wait_pause
import random

def learn_spells(character:dict, file_path:str="data/spells.json")->None:
    print("You begin your magic lessons at Hogwarts...")
    spells = load_file(file_path)
    remaining = {
        "Utility":3,
        "Defensive":1,
        "Offensive":1
    }
    is_remaining = True
    while is_remaining:
        selected_spell = spells[random.randint(0, len(spells)-1)]
        if remaining[selected_spell['type']] > 0:
            remaining[selected_spell["type"]] -= 1
            spells.remove(selected_spell)
            add_item(character, "Spells", f"{selected_spell["name"]} ({selected_spell["type"]}): {selected_spell["description"]}")
            print(f"You have just learned the spell: {selected_spell["name"]} ({selected_spell["type"]})")
            input("Press Enter to continue...")
        if remaining["Utility"] == 0 and remaining["Defensive"] == 0 and remaining["Offensive"] == 0:
            is_remaining = False
    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:\n")
    for spell in character["Spells"]:
        print("-",spell)

def magic_quiz(character:dict, file_path="data/magic_quiz.json")->int:
    quiz = load_file(file_path)
    points = 0
    print_bar()
    print("\nWelcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house")
    wait_pause()
    print()
    for i in range(4):
        question = random.choice(quiz)
        quiz.remove(question)
        print(f"{i+1}. {question["question"]}")
        answer = ask_text(">")
        if answer == question["answer"]:
            print(f"Correct answer {character["First Name"]} ! +25 points for your house.")
            points += 25
        else:
            print(f"Wrong answer {character["First Name"]} . The correct answer was:", question["answer"])
    print("Score obtained:", points)
    wait_pause()
    return points

def start_chapter_3(character, houses):
    print("=========== CHAPTER 3 : Classes and Discovering Hogwarts ===========")
    learn_spells(character)
    score = magic_quiz(character)
    update_house_points(houses, character["House"], score)
    display_winning_house(houses)
    wait_pause()
    display_character(character)
    wait_pause()
    print_bar()
    print("End of Chapter 3! You are now very good at magic, aren't you ?")