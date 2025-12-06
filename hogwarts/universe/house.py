from hogwarts.utils.input_utils import ask_choice


def update_house_points(houses:dict, house_name:str, points:int)->None:
    if not house_name in houses:
        print(f"[WARN] - HOUSE_UPDATE_POINTS - The House '{house_name}' don't exist")
    else:
        houses[house_name] += points
        print(f"+{points} for {house_name}! Total: {houses[house_name]} points")
    return

def display_winning_house(houses:dict)->None:
    max_value = None
    winners = []
    for name, value in houses.items():
        if max_value is None:
            max_value = value
            winners.append(name)
        else:
            if max_value < value or max_value is None:
                winners.clear()
                max_value = value
                winners.append(name)
            elif max_value == value:
                winners.append(name)

    if len(winners) == 0:
        print("[WARN] - HOUSE_DISPLAY_WINNING_HOUSE - House list is empty")
    elif len(winners) == 1:
        print(f"The house with the highest score is {winners[0]} with {max_value} points.")
    else:
        print(f"It's a tie ! The houses with the highest score are : {', '.join(winners)} with {max_value} points.")

def assign_house(character:dict, questions:list[tuple[str, list[str], list[str]]])->None:
    houses_points = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }


    for question in questions:
        value = ask_choice(question[0], question[1])
        houses_points[question[2][value - 1]] += 3
        print()

    for attribute, value in character["Attributes"].items():
        if attribute == "Courage":
            houses_points["Gryffindor"] += value*2
        elif attribute == "Ambition":
            houses_points["Slytherin"] += value*2
        elif attribute == "Loyalty":
            houses_points["Hufflepuff"] += value*2
        elif attribute == "Intelligence":
            houses_points["Ravenclaw"] += value*2

    house_selected = None
    max_value = None
    print("Summary of scores :")
    for house, value in houses_points.items():
        print(f"{house}: {value} points")
        if max_value is None:
            max_value = value
            house_selected = house
            continue
        if max_value < value:
            max_value = value
            house_selected = house

    return house_selected

