#funciton to demonstrate how loops works
#01 - using while
#i = 0
#while i < 3:
#    print("meow")
#    i += 1

#02 - using for
#for _ in range(8):
#    print("meow")

#03 - version using only print
#print("meow\n" * 3, end="")

#04 - using while true
#while True:
#    n = int(input("What's n? "))
#    if n > 0:
#        break

#for _ in range(n):
#    print("meow")

#05 - creating a meow function - hardcode version
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()