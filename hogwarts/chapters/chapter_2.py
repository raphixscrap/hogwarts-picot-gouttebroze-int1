from hogwarts.utils.input_utils import ask_text, ask_number, ask_choice, print_bar, load_file

def meet_friends(character: dict)->None:
    print("Red-heared boy : 'Hi! I'm Ron Weasley, mind if I sit with you?")
    if(ask_choice("How do you respond?",["Sure, have a seat !","Sorry, i prefer to travel alone"])==1):
        print("Ron smiles : -Awesome! You'll see, Hogwarts is amazing!")
        character["Attributes"]["Loyalty"]+=1
        ron = True
    else:
        print('Run stare at you for a moment : -Okay... enjoy your loneliness\n He closes the door and you see him walk away.')
        character["Attributes"]["Ambition"]+=1
    input('(...)')
    print("\n\n\n\n\n\n\n")
    print_bar()
    print('A girl enters next, already carrying a stack of books.')
    print('-Hello, I am Hermione Granger. Have you ever read "A History of Magic?')
    if (ask_choice("How do you respond?",["Yes, the autor trully knows his subject. It is a great introductive book!","Uh...no,I prefer adventures over books."])==1):
        print("Hermoine smiles, impressed : -Oh, finally someone you read the books we will study!")
        character['Attributes']["Intelligence"] +=1
    else:
        print("Hermoine walk away...")
        character["Attributes"]["Courage"]+=1

    input('(...)')
    print('\n\n\n\n\n\n\n')
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
        character["Attributes"]["Loyaty"] += 1
    else:
        print('My daddy will hear of this !')
        character["Attributes"]["Courage"] += 1
    print("Draco walks away... Without closing the door.")
    return
