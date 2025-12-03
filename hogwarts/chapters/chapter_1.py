from hogwarts.universe.character import init_character, display_character, show_character_money, modify_money, add_item
from hogwarts.utils.input_utils import ask_text, ask_number, ask_choice, print_bar, load_file


def introduction()->None:
    """
    This function introduce the story to the player and wait an input from the user to return.
    :return: None
    """
    print("As a kid, you always had been chasing for adventures and discoveries. You are living in a peaceful house a hundred miles away from London.")
    input("(...)")
    print("You are 12 years old and preparing to enter in middle school. But you don't know the great journey you are about to live...")
    input("(...)")
    return


def create_character()->dict:
    name = ask_text("Enter your character's last name")
    first_name = ask_text("Enter your character's first name")
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
        #TODO: Rewrite the contents of this
        print("Perfect ! You start to pack your stuff despite the disapprovement of your Uncle and Aunt !")

def meet_hagrid(character : dict)->None:
    print("Hagrid : 'Hello {}! I'm here to help you shopping on Diagon Alley.".format(character["First Name"]))
    if (ask_choice("Do you want to follow this unknown and menacing man named 'Hagrid'?",["Yes, for sure! What could go wrong ?","No, my mom always told me to avoid discussion with stangers."]) == 1):
        print("Hagrid take you out of the house, and the yells of uncle Vernon will not influence your decision.")
    else:
        print("Hagrid grab your shoulders and say with a concern glance : 'You have no choice {}!'. Then, he takes you along, and it's not with your strengh or uncle Vernon courage that will save you. ".format(character["First Name"]))
    input("(...)")
    return



def buy_supplies(character:dict)->dict:
    inventory = load_file("hogwarts/data/inventory.json")
    required = ["1","2","4"]
    remainingItems = []
    print("\033[1mWelcome to Diagon Alley!\033[0m")
    print("\nCatalog of available items:")
    for number, item in inventory.items():
        req="\n"
        if number in required:
            req="(required)\n"
            remainingItems.append(item[0])
        print(number + ".", item[0],"-",item[1],"Galleons ", end=req)
    successItem = False
    stillBuying = True
    while stillBuying:
        print()
        show_character_money(character)
        print('Remaining required items:',", ".join(remainingItems))
        selectedItemNumber = ask_number("Enter the number of the item to buy", 1,len(inventory))
        selectedItem = inventory[str(selectedItemNumber)]
        if selectedItem[1] > character["Money"]:
            print("You don't have enough money to buy :",selectedItem[0])
            stillBuying = False
        else:
            print("You bought:", selectedItem[0],f'(-{selectedItem[1]} Galleons)')
            modify_money(character, -selectedItem[1])
            add_item(character, "Inventory", selectedItem[0])
            if selectedItem[0] in remainingItems:
                remainingItems.remove(selectedItem[0])
        if len(remainingItems) == 0:
            successItem = True
            stillBuying = False
    if not successItem:
        print("You don't have the required equipment for your magic courses ! Game over...")
        exit()
    print("All required items have been purchased!")
    print("\nIt's time to choose your Hogwarts pet!\n")
    show_character_money(character)
    print()
    animals_choices = []
    print("Available pets:")
    animals = {
        "1":["Owl",20],
        "2":["Cat",15],
        "3":["Rat",10],
        "4":["Toad",5]
    }
    for number, item in animals.items():
        print(f'{number}. {item[0]} - {item[1]} Galleons')
        animals_choices.append(item[0])

    selectedAnimalNumber = ask_choice("Which pet do you want?", animals_choices)
    selectedAnimal = animals[str(selectedAnimalNumber)]
    if selectedAnimal[1] > character["Money"]:
        print("You don't have enough money to buy :", selectedAnimal[0])
        print("You don't have your Hogwarts pet ! You will feel so lonely ... Game over")
        exit()
    else:
        add_item(character, "Inventory", selectedAnimal[0])
        modify_money(character, -selectedAnimal[1])
        print(f"You chose: {selectedAnimal[0]} (-{selectedAnimal[1]} Galleons)")

    print("All required items have been successfully purchased! Here is your final inventory:\n")
    display_character(character)
    return character

def start_chapter_1()->dict:
    introduction()
    character = create_character()
    recieve_letter()
    meet_hagrid(character)
    character=buy_supplies(character)
    print_bar()
    print("End of Chapter 1! Your adventure begins at Hogwarts...")
    return character