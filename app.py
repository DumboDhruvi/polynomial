"""
This implements a command prompt application for the polynomial class i have created,

"""

import polynomial

memory = {}  # to save the polynomials


def exists(name: str) -> bool:  # just for code reuse lol!
    if name in memory.keys():
        return True
    else:
        return False


def create():  # does what it says
    name = input("name of polynomial: ").strip()
    if name in memory.keys():
        print("name already used! delete it or use another name!")
        create()
    print("enter power followed by coefficient seperated by space")
    try:
        poly = list(map(int, input("Enter: ").strip().split(" ")))
    except TypeError:
        create()
    else:
        memory[name] = polynomial.Polynomial(poly)
        print("Done!")


def show():
    print("currently loaded in memory: ")
    for i in memory.keys():
        print(i, ": ", memory[i])


def delete():
    dele = input("Input the name of the file to be deleted: ").strip()
    if dele in memory.keys():
        del memory[dele]
        print("Done!")
    else:
        print("no such polynomial exists")


def add(sign="+"):  # does both addition and subtraction and mutiplication!
    poly1, poly2 = input("Enter name of polynomial one & two seperated by space").strip().split(" ")
    if exists(poly2) and exists(poly1) and sign == "+":
        memory[poly1 + poly2 + "result_Add"] = memory[poly1] + memory[poly2]
        print("Your result is", memory[poly1 + poly2 + "result_Add"])
    elif exists(poly2) and exists(poly1) and sign == "-":
        memory[poly1 + poly2 + "result_Sub"] = memory[poly1] - memory[poly2]
        print("Your result is", memory[poly1 + poly2 + "result_Sub"])
    elif exists(poly2) and exists(poly1) and sign == "*":
        memory[poly1 + poly2 + "result_mul"] = memory[poly1] * memory[poly2]
        print("Your result is", memory[poly1 + poly2 + "result_mul"])
    else:
        if exists(poly1):
            print("polynomial 1st or both does not exist, create it 1st")
        else:
            print("polynomial 2nd does not exist, create it")


def evala():
    poly = input("Enter the name of polynomial to be evaluated: ").strip()
    if not exists(poly):
        print("polynomial does not exists")
        evala()
    val = int(input("Enter values for which you wanted evaluation: ").strip())
    print(memory[poly].evaluate(val))


def diffren():
    poly = input("Enter the name of polynomial to be differentiated: ").strip()
    if not exists(poly):
        print("polynomial does not exists")
        diffren()
    memory[poly + "diffrentiation"] = memory[poly].differentiation()
    print(memory[poly + "diffrentiation"])


def intregrate():
    poly = input("Enter the name of polynomial to be intregrated: ").strip()
    if not exists(poly):
        print("polynomial does not exists")
        intregrate()
    memory[poly + "integration"] = memory[poly].integration()
    print(memory[poly + "integration"])


def input_(wrong=""):
    list_commands = ["create", "add", "sub", "mul", "differentiate", "intregrate", "show", "eval", "exit", "delete"]
    intro(wrong, list_commands)
    command = input("Enter :")
    if command not in list_commands:
        return input_("wrong")
    else:
        return command


def intro(s: str, l1):
    if not s:
        print("hello", l1)
    elif s:
        print(s)


def app():
    while True:
        command = input_().strip()
        if command == "create":
            create()
        elif command == "add":
            add()
        elif command == "sub":
            add("-")
        elif command == "mul":
            add("*")
        elif command == "show":
            show()
        elif command == "eval":
            evala()
        elif command == "delete":
            delete()
        elif command == "differentiate":
            diffren()
        elif command == "intregrate":
            intregrate()
        elif command == "exit":
            print("Have a nice day bye!")
            break


if __name__ == "__main__":
    app()
