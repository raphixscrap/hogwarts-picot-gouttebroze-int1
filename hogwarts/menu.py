from hogwarts.chapters.chapter_1 import start_chapter_1
from hogwarts.chapters.chapter_2 import start_chapter_2
from hogwarts.chapters.chapter_3 import start_chapter_3
from hogwarts.utils.input_utils import ask_number


def display_main_menu()->None:
    print("1. Start Chapter 1 - Arrival in the magical world")
    print("2. Exit the game")

def launch_menu_choice()->None:
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }
    display_main_menu()
    while True:
        choice = ask_number("Your choice")
        if choice == 2:
            print("Goodbye Wizzard ! Don't forget : magic is the key !")
            exit()
        elif choice == 1:
            character = start_chapter_1()
            start_chapter_2(character)
            start_chapter_3(character, houses)
            exit()
        else:
            print("Invalid choice, choose again !")
