def ask_text(message: str)->str:
    """
    This function ask the user for a string and return the user answer without spaces.
    :param message: type -> str, This message will be displayed before the user enter his answer.
    :return: type -> str, the returned value is the answer of the user but without spaces.
    """
    value = ""
    while value.strip() == "":
        value = input(message + " : ")
    return value

def ask_number(message: str, min_val=None, max_val=None) -> int:
    """
    This function asks the user to enter a number and make sure the number is valid based on the type and the value.
    :param message: type -> str, this message will be displayed to help the user in his choice of number.
    :param min_val: type -> int, optional parameter that indicates if you want the value to greater or equal than your minimum.
    :param max_val: type -> int, optional parameter that indicates if you want the value to be lesser or equal than your maximum.
    :return: type-> int, the returned value is the number chosen by the user.
    """
    value = ask_text(message+" : ")
    try:
        int_value=int(value)
        if (min_val is None and max_val is None):
            return int_value
        elif (min_val is None and max_val < int_value):
            raise ValueError
        elif (max_val is None and min_val > int_value):
            raise ValueError
        elif (not min_val <= int_value <= max_val):
            raise ValueError
    except ValueError:
        return ask_number(message,min_val,max_val)
    except TypeError:
        return ask_number(message, min_val, max_val)
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
    try:
        user_choice = int(input("Your choice:\t"))
        if (user_choice<1 and user_choice>len(options)):
            raise ValueError
    except :
        return ask_choice(message,options)
    return user_choice
