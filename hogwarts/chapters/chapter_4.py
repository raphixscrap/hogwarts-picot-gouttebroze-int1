import random

from hogwarts.universe.character import display_character
from hogwarts.universe.house import display_winning_house, update_house_points
from hogwarts.utils.input_utils import print_bar, load_file


def create_team(house:str, team_data:dict,is_player:bool=False, player:dict=None)->dict:
    players = []
    if is_player and player:
        players.append(f'{player["First Name"]} {player["Last Name"]} (Seeker)')
        for i in range(1,len(team_data["players"])):
            players.append(team_data["players"][i])
    else:
        players = team_data["players"]
    team = {
        'name':house,
        'score':0,
        'goals_scored':0,
        'goals_blocked':0,
        'caught_snitch': False,
        'players':players
    }
    return team

def attempt_goal(attacking_team:dict, defending_team:dict, player_is_seeker=False)->None:
    chance_goal = random.randint(1, 10)
    if chance_goal >= 6:
        player_attack = attacking_team["players"][random.randint(0,len(attacking_team["players"]) - 1)]
        if player_is_seeker:
            player_attack = attacking_team["players"][0]
        attacking_team["goals_scored"] += 1
        attacking_team["score"] += 10
        print(f"{player_attack} scores a goal for {attacking_team["name"]} (+10 points)")
    else:
        defending_team["goals_blocked"] += 1
        print(f"{defending_team["name"]} blocks the attack!")

def golden_snitch_appears()->int:
    dice = random.randint(1,6)
    return dice == 6

def catch_golden_snitch(e1:dict, e2:dict)->dict:
    winner = random.choice([e1, e2])
    winner["caught_snitch"] = True
    winner['score'] += 150
    return winner

def display_score(e1:dict, e2:dict)->None:
    print("Current score :")
    print(f"→ {e1["name"]}: {e1["score"]} points")
    print(f"→ {e2["name"]}: {e2["score"]} points")

def display_team(house:str, team:list):
    print(house, "team:")
    for i in range(len(team)):
        print(" -", team[i])

def quidditch_match(character: dict, houses:dict)->None:
    teams = load_file("hogwarts/data/teams_quidditch.json")
    c_team = create_team(character["House"], teams[character["House"]], True, character)
    del teams[character["House"]]
    o_name = random.choice(list(teams.keys()))
    o_team = create_team(o_name, teams[o_name])
    winner = None
    print("Quidditch Match:", c_team["name"], "vs", o_team["name"],"!")

    display_team(c_team["name"], c_team["players"])
    print("\n")
    display_team(o_team['name'], o_team["players"])
    print("\nYou are playing for", c_team["name"], "as the Seeker\n")
    input("(...)")
    for i in range(20):
        print("━━━","Turn",i + 1,"━━━")
        attempt_goal(c_team, o_team, True)
        attempt_goal(o_team, c_team)
        print()
        display_score(c_team, o_team)
        if golden_snitch_appears():
            winner = catch_golden_snitch(c_team, o_team)
            print("The Golden Snitch has been caught by", winner["name"], "(+150 points)")
            break;
        input("Press Enter to continue")
    print("End of the match!\n")
    display_score(c_team, o_team)
    input("(...)")
    print("Final result:")
    if winner:
        print(f"The Golden Snitch was caught by {winner["name"]}!")
        update_house_points(houses, winner["name"], 150)
        display_winning_house(houses)
    c_score = c_team['score']
    o_score = o_team["score"]

    if(c_score > o_score):
        winner = c_team
    elif(c_score < o_score):
        winner = o_team

    if winner is None:
        print("It's a tie ! No one wins the game !")
    else:
        print(f'Victory for {winner["name"]}!')
        update_house_points(houses, winner["name"], 500)

    input("(...)")



def start_chapter_4_quidditch(character, houses)->None:
    print("=========== CHAPTER 4 : The Quidditch Match ===========")
    quidditch_match(character, houses)
    print_bar()
    print("End of Chapter 4! What an incredible performance on the field!")
    input("(...)")
    display_winning_house(houses)
    input("(...)")
    display_character(character)
    input("(...)")
    print_bar()
