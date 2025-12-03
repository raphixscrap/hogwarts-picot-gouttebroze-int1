from hogwarts.universe.character import init_character, display_character
from hogwarts.utils.input_utils import ask_text, ask_number, ask_choice, print_bar, load_file


def introduction()->None:
    """
    This function introduce the story to the player and wait an input from the user to return.
    :return: None
    """
    print("As a kid, you always had been chasing for adventures and discoveries. You are living in a peaceful house a hundred miles away from London.")
    input("Enter any cases to continue :\t")
    print("You are 12 years old and preparing to enter in middle school. But you don't know the great journey you are about to live...")
    input("Enter any cases to continue :\t")
    return


def create_character()->dict:
    name = ask_text("Enter your character's last name")
    first_name = ask_text("Enter your character's last name")
    print("\nChoose your attributes :")
    courage = ask_number("Courage level (1-10)", 1,10)
    intelligence = ask_number("Intelligence level (1-10)", 1, 10)
    loyalty = ask_number("Loyalty level (1-10)", 1, 10)
    ambition = ask_number("Ambition level (1-10)", 1, 10)
    character = init_character(name, first_name, {
        "Courage":courage,
        "Intelligence":intelligence,
        "Loyalty":loyalty,
        "Ambition":ambition
    })
    display_character(character)
    return character

def recieve_letter()->None:
    print("An owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    print("Dear Student,\n\nWe are pleased to inform you that you have been accepted to Hogwarts School of Witchcraft and Wizardry!”\n")
    if ask_choice("Do you accept this invitation and go to Hogwarts?",["Yes of course !", "No, I'd rather stay with Uncle Vernon..."]) == 2:
        print("\nYou tear up the letter, and Uncle Vernon cheers:")
        print("\n“EXCELLENT! Finally, someone NORMAL in this house!”")
        print("\nThe magical world will never know you existed... Game over.")
        exit()
    else:
        print("Test")

def meet_hagrid(character : dict)->None:
    print("Hagrid : 'Hello {}! I'm here to help you shopping on Diagon Alley.".format(character["First Name"]))
    if (ask_choice("Do you want to follow this unknown and menacing man named 'Hagrid'?",["Yes, for sure! What could go wrong ?","No, my mom always told me to avoid discussion with stangers."]) == 1):
        print("Hagrid take you out of the house, and the yells of uncle Vernon will not influence your decision.")
    else:
        print("Hagrid grab your shoulders and say with a concern glance : 'You have no choice {}!'. Then, he takes you along, and it's not with your strengh or uncle Vernon courage that will save you. ")
    input("Enter any cases to continue : \t")
    return
