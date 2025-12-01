def init_character(last_name :str, first_name :str, attributes :dict)->dict:
    return {"Last Name": last_name, "First Name": first_name, "Money": 100, "Inventory": [], "Spells": [], "Attributes":attributes}

def display_character (character : dict)->None:
    print("Character profile: ")
    for key,item in character.items():
        if(type(item) == list):
            print("{}: {}".format(key," ; ".join(item)))
        elif(type(item)==dict):
            print("{} :".format(key))
            for item_key, item_item in item.items():
                print(" - {}: {}".format(item_key,item_item))
        else:
            print("{}: {}".format(key,item))
    return

def get_full_name(character:dict)->str:
    return character["First Name"] + character["Last Name"]


def modify_money(character : dict, money :int)->dict:
    character["Money"] += money
    return character

def add_item(character:dict, key:str, item:str)->dict:
    if key != "Inventory" and key != "Spells":
        print(f"[WARN] - CHARACTER_ADD_ITEM - Key is invalid for adding an item for {get_full_name(character)}")
    else:
        character[key].append(item)
    return character

