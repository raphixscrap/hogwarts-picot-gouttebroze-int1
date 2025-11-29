def update_house_points(houses:dict, house_name:str, points:int)->None:
    if not house_name in houses:
        print(f"[WARN] - HOUSE_UPDATE_POINTS - The House '{house_name}' don't exist")
    else:
        houses[house_name] += points
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
        print("[WARN] - HOUSE_DISPLAY_WINNING_HOUSE - House list empty")
    elif len(winners) == 1:
        print(f"The house with the highest score is {winners[0]} with {max_value} points.")
    else:
        print(f"The houses with the highest score are : {', '.join(winners)} with {max_value} points.")

def assign_house(character:dict, questions:list[tuple[str, list[str], list[str]]])->None:
    pass

