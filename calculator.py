# return true, if string is a rational number
def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


print("Hello in my calculator. Type in:\n"
      "- integer operand,\n"
      "- operator (\'+\', \'-\', \'*\', \'/\', \'**\'(pow)), \n"
      "- one more integer operand."
      "Type exit to exit.")
stop = False
while not stop:
    try:

        #input and check of a
        nextInput = False
        while not nextInput:
            a = input()
            a = a.strip()
            if a == "exit":
                stop = True
                nextInput = True
                continue
            if not is_digit(a):
                print("This string isn't a digit.\n")
            else:
                nextInput = True
        if a == "exit":
            continue

        # input and check of operator
        nextInput = False
        while not nextInput:
            operator = input()
            operator = operator.strip()
            if operator == "exit":
                stop = True
                nextInput = True
                continue
            if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "**":
                print("This string isn't an available operator(\'+\', \'-\', \'*\', \'/\', \'**\'(pow)).\n")
            else:
                nextInput = True
        if operator == "exit":
            continue

        # input and check of b
        nextInput = False
        while not nextInput:
            b = input()
            b = b.strip()
            if b == "exit":
                stop = True
                nextInput = True
                continue
            if not is_digit(b):
                print("This string isn't a digit.\n")
            else:
                nextInput = True
        if b == "exit":
            continue

        if operator == "+":
            print(float(a) + float(b))
        elif operator == "-":
            print(float(a) - float(b))
        elif operator == "*":
            print(float(a) * float(b))
        elif operator == "/":
            print(float(a) / float(b))
        elif operator == "**":
            print(float(a) ** float(b))
    except:
        print("Something went wrong.")
print("Good bye!")
