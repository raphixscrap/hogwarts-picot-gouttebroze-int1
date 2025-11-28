def ask_test(message: str) -> str:
    value = ""
    while value.strip() == "":
        value = input(message)
    return value


def ask_number(message: str, min_val=None, max_val=None) -> int:
    negative = False
    accept_digits = "0123456789"
    value = None
    while value == None or value < min_val or value > max_val:
        value_input=input(message)
        for i in range(len(message)):
           if(i == 0 and message[i] == "-"):
               negative = True
           else:
               if(message[i] in accept_digits):
                   print("TEST")
               else:
                   break
    return value