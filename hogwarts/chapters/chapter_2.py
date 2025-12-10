from hogwarts.universe.character import display_character
from hogwarts.utils.input_utils import ask_text, ask_number, ask_choice, print_bar, load_file, wait_pause
from hogwarts.universe.house import assign_house

def meet_friends(character: dict)->None:
    print("Red-heared boy : 'Hi! I'm Ron Weasley, mind if I sit with you?")
    ron = False
    if(ask_choice("How do you respond?",["Sure, have a seat !","Sorry, i prefer to travel alone"])==1):
        print("Ron smiles : -Awesome! You'll see, Hogwarts is amazing!")
        character["Attributes"]["Loyalty"]+=1
        ron = True
    else:
        print('Run stare at you for a moment : -Okay... enjoy your loneliness\n He closes the door and you see him walk away.')
        character["Attributes"]["Ambition"]+=1
    wait_pause()
    print("\n\n\n")
    print_bar()
    print('A girl enters next, already carrying a stack of books.')
    print('-Hello, I am Hermione Granger. Have you ever read "A History of Magic?')
    if (ask_choice("How do you respond?",["Yes, the autor trully knows his subject. It is a great introductive book!","Uh...no,I prefer adventures over books."])==1):
        print("Hermoine smiles, impressed : -Oh, finally someone you read the books we will study!")
        character['Attributes']["Intelligence"] +=1
    else:
        print("Hermoine walk away...")
        character["Attributes"]["Courage"]+=1

    wait_pause()
    print('\n\n\n')
    print_bar()
    print(" The door slams open, and a blonde boy enter, with an dedain glance, he asks :")
    print("-I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    if ron:
        print("He looks at Ron and makes a face.")
    u_choice = ask_choice("How do you respond?",["Shake his hand politely.",'Ignore him completely.','Respond with arrogance.'])
    if (u_choice==1):
        print('He smiles: -Hope you will make the right choice...')
        character["Attributes"]["Ambition"]+=1
    elif (u_choice == 2):
        print("Draco frowns, annoyed. — You'll regret that!")
        character["Attributes"]["Loyalty"] += 1
    else:
        print('My daddy will hear of this !')
        character["Attributes"]["Courage"] += 1
    print("Draco walks away... Without closing the door.")
    return

def welcome_message()->None:
    print_bar()
    print("\nWelcome to Hogwarts, a sanctuary where your minds will be sharpened and your hearts shall find a home.")
    wait_pause()
    print("May you fill these ancient halls with friendship, for help will always be given here to those who ask for it.")
    wait_pause()
    print("Remember that happiness can be found, even in the darkest of times, if one only remembers to turn on the light.")
    wait_pause()
    print("Now, before we become too befuddled by our own brilliance, let the feast begin!")

def sorting_ceremony(character:dict)->dict:
    print_bar()
    print("\nThe sorting ceremony begins in the Great Hall...")
    print("\nThe Sorting Hat observes you for a long time before asking its questions:")
    wait_pause()
    print("\n")
    questions = [
        (
            "Which subject at Hogwarts interests you the most?",
            ["Defense Against the Dark Arts", "Potions", "Herbology", "History of Magic"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "You find a locked door in a mysterious corridor. What do you do?",
            ["Try to break it down", "Pick the lock quietly", "Knock and ask if anyone is there",
             "Look for a key or solve the riddle"],
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
    selected = assign_house(character, questions)
    character["House"]=selected
    print("\nThe Sorting Hat exclaims:",selected)
    print(f"You join the {selected} students to loud cheers !")
    input("(...)\n")
    return character

def enter_common_room(character:dict)->None:
    if not character["House"]:
        print("[WARN] - The House is not set for the character")
        return
    houses_data = load_file("data/houses.json")
    house= houses_data[character["House"]]
    print_bar()
    print("\nYou follow the perfects though the castle corridors...")
    wait_pause()
    print(house["emoji"], house["description"])
    wait_pause()
    print(house["installation_message"])
    print("\nYour house colors:", ", ".join(house["colors"]))
    wait_pause()

def start_chapter_2(character:dict)->None:
    print("=========== CHAPTER 2 : The journey to Hogwarts ===========")
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)
    display_character(character)
    wait_pause()
    print_bar()
    print("End of Chapter 2! The classes at Hogwarts will now start ! Are you ready to learn magic ?")