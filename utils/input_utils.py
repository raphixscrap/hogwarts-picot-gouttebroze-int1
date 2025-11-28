def ask_text(message: str)->str:
    value = ""
    while value.strip() == "":
        value = input(message)
    return value

def ask_number(message: str, min_val=None, max_val=None) -> int:
    value = ask_text(message)
    int_value = 0
    digits = "1234567890"
    negative = False
    if (value[0] == "-"):
        negative = True
        value = value[1:]
    for i in range (len(value)):
        if(value[i] in digits):
            int_value += (ord(value[i])-ord('0'))*10**(len(value)-i-1)
        else :
            if(min_val is None and max_val is None):
                print("Please enter a number.")
            elif(min_val is None and not max_val is None):
                print("Please enter a number lesser or equal to {}.".format(max_val))
            elif(not min_val is None and max_val is None):
                print("Please enter a number greater or equal to {}.".format(min_val))
            else:
                print("Please enter a number between {} and {}.".format(min_val,max_val))
            return ask_number(message,min_val,max_val)
    if (negative):
        int_value *= -1
    if(min_val is None and max_val is None):
        return int_value
    elif(min_val is None and max_val<int_value):
        print("Please enter a number lesser or equal to {}.".format(max_val))
        return ask_number(message, min_val, max_val)
    elif(max_val is None and min_val>int_value):
        print("Please enter a number greater or equal to {}.".format(min_val))
        return ask_number(message, min_val, max_val)
    elif (not min_val<=int_value<=max_val):
        print("Please enter a number between {} and {}.".format(min_val,max_val))
        return ask_number(message, min_val, max_val)
    return int_value

def ask_choice(message :str, options :list)->int:
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
