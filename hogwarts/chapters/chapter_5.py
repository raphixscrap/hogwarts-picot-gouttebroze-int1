from hogwarts.utils.input_utils import wait_pause, ask_choice, print_bar, clean_board
from random import randint


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

def print_status(character,enemy):
    print("Your enemy as {}/{} HP.".format(enemy["HP"],enemy["MAX_HP"]))
    print("["+'='*(10-(enemy["MAX_HP"]-enemy["HP"])//2)+"]")
    print('\n'*2)
    print("You have {}/{} HP.".format(character["HP"],character["MAX_HP"]))
    print("[" + '=' * (10 - (character["MAX_HP"] - character["HP"]) // 2) + "]")

def attack (caster, target):
    damage = 0
    for _ in range (caster['Attack'][0]):
        damage += randint(1,caster['Attack'][1])
    target["HP"]-= damage
    if(target["HP"]<0):
        target["HP"]=0
    return

def turn(character, enemy):
    print_status(character, enemy)
    player_protect,character_dodge = False,5
    enemy_protect,enemy_dodge = False,5
    player_action = ask_choice("What do you want to do ?",["ATTACK","PROTEGO","DODGE"])
    enemy_action = randint(2,6)
    if(enemy_action==5):
        enemy_protect=True
    elif(enemy_action ==3):
        enemy_dodge*=16

    if(player_action == 1):
        if(enemy_protect):
            print("{} uses protego, you're attack is parried".format(enemy["name"]))
            if(randint(1,100)%2 == 0):
                print('{} is counterattacking !'.format(enemy["name"]))
                if (character_dodge >= randint(1,100)):
                    print("But you dodged it !")
                else:
                    attack(enemy,character)
        else:
            if(enemy_dodge >= randint(1,100)):
                print("{} dodge it!".format(enemy["name"]))
            else:
                attack(character,enemy)
    elif(player_action == 2):
        player_protect = True
    else:
        character_dodge *= 16
    wait_pause()
    if(enemy_action!=5 and enemy_action!=3):
        if(player_protect):
            print('The enemy tries to attack you when you use protego!')
            if (randint(1,100)%2 ==0):
                print("You counterattack !")
                if(enemy_dodge >= randint(1,100)):
                    print("But {} dodge it ".format(enemy["name"]))
                else:
                    attack(character,enemy)
        else:
            if(character_dodge >= randint(1,100)):
                print("You dodge the enemy's attack !")
            else:
                attack(enemy,character)
    return

def fight(character_duel, enemy_duel)->str:
    while(character_duel['HP']!=0 and enemy_duel["HP"]!=0):
        turn(character_duel,enemy_duel)
    if(character_duel['HP']!=0):
        print("YOU WON THIS DUEL !")
        return character_duel['name']
    else:
        print("YOU LOST THIS DUEL !")
        return enemy_duel["name"]

def tutorial_fight(character:dict):
    training_enemy = {"name":"Training bot","HP":20,'MAX_HP':20,'Attack':[2,4]}
    character_duel = {"name":character["First Name"],"HP":20,'MAX_HP':20,"Attack":[character["Attributes"]["Ambition"]%2+1,character["Attributes"]["Intelligence"]+1]}
    fight(character_duel,training_enemy)

def tutorial (character:dict):
    print("This tutorial is here to explain how to play a duel in our game.")
    wait_pause()
    explanation()
    while( ask_choice("Do you want to make a first duel to understand how it works?",["yes","No"])==1):
        tutorial_fight(character)

def script (character:dict):
    print('After years at Hogwarts, you successfully pass your years.')
    print('In your 6th year, you are allowed to participate to the Goblet of fire championship.')
    wait_pause()
    print("After passing the different competition, you find yourself in the maze.")
    print("After minutes of running in the maze you finally find the cup!")
    wait_pause()
    print('You run to it but when you touch it...')
    wait_pause()
    print('You are teleported to a graveyard.')
    print("A man, with a silk Habotai over-robe...")
    print("Mysterious man : \"There you are {}".format(character['First Name']))
    print("IT'S THE DARK LORD HIMSELF !")
    print("You grab your magic wand and prepare yourself for a fight you are not sure to survive.")

def duel_dark_lord(character):
    character_duel = {'name':character["First Name"],'HP':10*character["Attributes"]["Ambition"],'MAX_HP':10*character["Attributes"]["Ambition"],"Attack":[character["Attributes"]["Ambition"]%2+1,character["Attributes"]["Intelligence"]+1]}
    dark_lord = {"name":"Voldemort",'HP':30,'MAX_HP':35,'Attack':[3,4]}
    winner = fight(character_duel,dark_lord)

    if(winner!= character["First Name"]):
        print("The dark lord laughs as your last forces leave you.")
        print("\" You were so weak {}!\"".format(character["First Name"]))
        print("No one will know about what happened... Your friends will try to find you... But will never find your body...")
        wait_pause()
        print("The dark lord still alive... and no one know he is back...")
        print_bar()

    else:
        print("As the dark lord seems stunned by your attack, you jump to catch the cup.")
        print("The cup bring you back at Hogwarts, you are seriously injured by your duel...")
        wait_pause()
        print("The last words you say before you collapse on the grass are :\" He is back\".\n And you close your eyes. Not for the last time but you feel how close you were from death.")
        wait_pause()

def start_chapter_5(character :dict):
    print("=========== CHAPTER 5 : Duel against Voldemort during the Goblet of Fire ===========")
    tutorial(character)
    clean_board()
    script(character)
    clean_board()
    duel_dark_lord(character)

    wait_pause()
    print_bar()
    print('Thanks for playing our game... You have finished the last chapter.')

