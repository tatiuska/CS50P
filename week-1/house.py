# program that tells which HP house you belong to
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # sintaxe para qualquer outra possibilidade não contemplada pelo match/case
    case _:
        print("Who?")    

