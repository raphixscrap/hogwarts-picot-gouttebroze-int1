def ask_text(message: str)->str:
    value = ""
    while value.strip() == "":
        value = input(message)
    return value


def ask_number(message: str, min_val=None, max_val=None) -> int:
    negative = False
    accept_digits = "0123456789"
    value = None
    while value is None or value < min_val or value > max_val:
        value_input=input(message)
        for i in range(len(value_input)):
           if(i == 0 and value_input[i] == "-"):
               negative = True
           else:
               if(not value_input[i] in accept_digits):

               else:
                   break
    return value