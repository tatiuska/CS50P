# Creating main function
def main():
    # Ask user for their name
    name = input("What's your name? ")
    goodbye(name)


# Creating the function hello
def goodbye(to="world"):
    print("Goodbye,", to)

main()
