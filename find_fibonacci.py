def fibonacci():
    n = int(input("Enter your number: "))
    a = 0
    b = 1
    c = 1
    if n == 0 or n == 1:
        print(str(n) + "  is a fibonacci number")
        option()
    while a < n:
        a = b + c
        c = b
        b = a
    if a == n:
        print(str(n) + "  is a fibonacci number")
        option()
    else:
        print(str(n) + " is not a fibonacci number")
        option()
def option():
    choice = str(input("Do you want to try again?(y/n): "))
    if choice == "y":
        fibonacci()
    if choice == "n":
        print("bye")
        quit()

fibonacci()