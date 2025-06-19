def leap():
    year = int(input("Enter your year: "))
    lol = year % 4
    if lol == 0:
        print(str(year) + " is a leap year")
    if lol != 0:
        print(str(year) + "is not a leap year")
    option()


def option():
    choice = input("Do you want to continue?(y/n): ")
    if choice == "y":
        leap()
    elif choice == "n":
        print("Bye")
        quit()
    else:
        print("Can't understand. Try again")
        option()


leap()
