from hogwarts.utils.input_utils import wait_pause

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


def tutorial (character:dict):
    print("This tutorial is here to explain how to play a duel in our game.")
    wait_pause()
    explanation()



def start_chapter_5(character :dict):
    print("=========== CHAPTER 5 : Duel against Voldemort during the Goblet of Fire ===========")
    tutorial(character)
    sceanario(character)
    duel_voldemort(character)

