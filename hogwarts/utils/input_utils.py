from json import load

def verif_number(string: str)->bool:
    string_copy = string
    if (string_copy[0] == "-"):
        string_copy = string_copy[1:]
    for letter in string_copy:
        if(not letter in "1234567890"):
            return False
    return True

def ask_text(message: str)->str:
    """
    This function ask the user for a string and return the user answer without spaces.
    :param message: type -> str, This message will be displayed before the user enter his answer.
    :return: type -> str, the returned value is the answer of the user but without spaces.
    """
    value = ""
    while value.strip() == "":
        value = input(message + ":\t")
    return value

def wait_pause()->None:
    input("(...)")

def ask_number(message: str, min_val=None, max_val=None) -> int:
    """
    This function asks the user to enter a number and make sure the number is valid based on the type and the value.
    :param message: type -> str, this message will be displayed to help the user in his choice of number.
    :param min_val: type -> int, optional parameter that indicates if you want the value to greater or equal than your minimum.
    :param max_val: type -> int, optional parameter that indicates if you want the value to be lesser or equal than your maximum.
    :return: type-> int, the returned value is the number chosen by the user.
    """
    value = ask_text(message)
    if (verif_number(value)):
        int_value=int(value)
    else :
        return ask_number(message,min_val,max_val)
    if (min_val is None and max_val is None):
        return int_value
    elif (min_val is None and max_val < int_value):
        return ask_number(message,min_val,max_val)
    elif (max_val is None and min_val > int_value):
        return ask_number(message,min_val,max_val)
    elif (not min_val <= int_value <= max_val):
        return ask_number(message,min_val,max_val)

    return int_value

def ask_choice(message :str, options :list)->int:
    """
    This function print the message given in parameter and display the options and treat the user answer to return his choice.
    :param message: type -> str, this parameter will be displayed before the different options.
    :param options: type -> list, this parameter regroup the different options you give to the user, the order count.
    :return: type-> int, the returned value corresponds to an index of options -1.
    """
    print(message)
    for i in range (len(options)):
        print("{}. {}".format(i+1,options[i]))

    user_choice = ask_number("Your choice", 1, len(options))
    return user_choice

def load_file(file_path : str):
    """
    This function extracts the data from a json file.
    :param file_path: type -> str, this string represents the path to access the json file.
    :return: type -> dict/list, the returned value is a dict or a list depending on the json file, it contains the data from the json file.
    """
    file = open(file_path,'r',encoding="utf-8")
    extracted_file = load(file)
    file.close()
    return extracted_file

def print_bar():
    print("\n-*#*-*#*-*#*-*#*-*#*-*#*-*#*-*#*-*#*-*#*-*#*-*#*-*#*-")

def clean_board():
    print('\n'*30)