from hogwarts.utils.input_utils import wait_pause, ask_choice


def explanation ():
    print("Duels are turn based fights.")
    print('In our game, there exist 3 kind of move you can make:')
    wait_pause()
    print('\t-Attack : You will cast a spell that causes damage to your enemy.')
    print("\t-Protego : You cast the spell \"Protego\" that will increase your chance of parrying enemy's spell for this turn.")
    print("\t-Dodge : You will increase you chance of dodging the enemy spell.")
    wait_pause()
    print('\n' * 5)
    print('Parrying gives you a chance to counterattack the enemy.')
    print('There exist a basic probability that you dodge enemy\'s attack even if you don\'t select the action "Dodge"')
    wait_pause()
    print('You win a duel if your enemy\'s life reach 0 and yours is superior to 0. And vice versa.')
    wait_pause()

def fight(character_duel, enemy_duel):
    while(character_duel['HP']!=0 and enemy_duel["HP"]!=0):
        turn(character_duel,enemy_duel)
    if(character_duel['HP']!=0):
        print("YOU WON THIS DUEL !")
    else:
        print("YOU LOST THIS DUEL !")

def tutorial_fight(character:dict):
    training_enemy = {"name":"Training bot","HP":20,'Attack':[2,4]}
    character_duel = {"Name":character["First Name"],"HP":20,"Attack":[character["Attributes"]["Ambition"]%2,character["Attributes"]["Intelligence"]]}
    fight(character_duel,training_enemy)

def tutorial (character:dict):
    print("This tutorial is here to explain how to play a duel in our game.")
    wait_pause()
    explanation()
    while( ask_choice("Do you want to make a first duel to understand how it works?",["yes","No"])==1):
        tutorial_fight(character)



def start_chapter_5(character :dict):
    print("=========== CHAPTER 5 : Duel against Voldemort during the Goblet of Fire ===========")
    tutorial(character)
    sceanario(character)
    duel_voldemort(character)

