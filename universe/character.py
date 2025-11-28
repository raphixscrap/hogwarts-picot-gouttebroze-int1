

def init_character(last_name :str, first_name :str, attributes :dict)->dict:
    return {"Last Name": last_name, "First Name": first_name, "Money": 100, "Inventory": [], "Attributes":attributes}

def display_character (character : dict)->None:
    print("Character profile: ")
    for key,item in character.items():
        if(type(item) == list):
            print("{}: {}".format(key," ; ".join(item)))
        elif(type(item)==dict):
            print("{} :".format(key))
            for item_key, item_item in item.keys():
                print(" - {}: {}".format(item_key,item_item))
        else:
            print("{}: {}".format(key,item))
    return