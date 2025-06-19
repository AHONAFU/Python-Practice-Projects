print("### The  Adventure Game?  ###\n\n")


def start():
    choice = input("Would you like to play the game?(yes/no): ")
    if choice == "yes":
        print("!sike ended with em. Lol stupid ass bitch")
        quit()
    elif choice == "no":
        level_1()
    else:
        print("I don't know what the  fuck you are talking about. Try again bitch")
        start()


def level_1():
    choice = input("Do you want to go left or right?: ")
    if choice == "left":
        print("There was nothing in the left side. You made the wrong choice")
        print("You ended with 0/10 points")
        quit()
    elif choice == "right":
        print("Good Choice!!")
        level_2()
    else:
        print("Do you know English? Then why are doing this wrong? Try again!!")
        level_1()


def level_2():
    print("Oh no! You came upon some warriors.")
    choice = input("What do you want to do?(run/attack): ")
    if choice == "run":
        print("Good choice but you are too afraid to fight.")
        print("You ended with 2.5/10 points")
        quit()
    elif choice == "attack":
        level_2else()
    else:
        print("Do you know English? Then why are doing this wrong? Try again!!")
        level_2()


def level_2else():
    choice_1 = input("How do you want to attack?(silently/bravely): ")
    if choice_1 == "bravely":
        print("Sometimes you just should not go straight. Take decision calmly dumbass")
        print("You ended with 2.5/10 points")
        quit()
    elif choice_1 == "silently":
        level2alpha()
    else:
        print("Do you know English? Then why are doing this wrong? Try again!!")
        level_2else()


def level2alpha():
    choice_2 = int(input("How much Damage do you want to make?(10/50/100): "))
    if choice_2 == 10:
        print("Wrong choice they were too powerful")
        print("You ended with 2.5/10 points")
        quit()
    elif choice_2 == 100:
        print("Wrong choice. You won the fight but you are out of energy. So you loose")
        print("You ended with 2.5/10 points")
        quit()
    elif choice_2 == 50:
        print("Wise Choice.")
        level_3()
    else:
        print("Do you know English? Then why are doing this wrong? Try again!!")
        level2alpha()


def level_3():
    print("Okay. Now you Came upon a river.")
    choice = input("What do you want to do? Pick Carefully(cross/leave): ")
    if choice == "leave":
        print("LOL i was not joking on this one XD")
        print("You ended with 5/10 points")
        quit()
    elif choice == "cross":
        level_3alpha()
    else:
        print("Do you know English? Then why are doing this wrong? Try again!!")
        level_3()


def level_3alpha():
    choice = input("Do you want to swim or take a boat?(swim/boat): ")
    if choice == "boat":
        print("Sorry the  boat sank. You lost")
        print("You ended with 5/10 points")
        quit()
    elif choice == "swim":
        print("Good job. You successfully swam a river but you ran out of energy.")
        level_4()
    else:
        print("Do you know English? Then why are doing this wrong? Try again!!")
        level_3alpha()


def level_4():
    choice = input("What do you wan to drink to hydrate your self?(water/coconut): ")
    if choice == "water":
        print("LOL there was some poison in the water. WASTED")
        print("You ended with 7.5/10  points")
        quit()
    elif choice == "coconut":
        print("Congratulations on choosing right drink. It was really healthy")
        print("You completed the game with full points")
        level_4alpha()
    else:
        print("Do you know English? Then why are doing this wrong? Try again!!")
        level_4()


def level_4alpha():
    choice_1 = input("Do you want to play the game again?:(yes/no): ")
    if choice_1 == "yes":
        start()
    elif choice_1 == "no":
        choice = input("Okay do you want to claim your prize?(yes/no): ")
        if choice == "no":
            print("Thanks for playing. BYE!!")
            quit()
        elif choice == "yes":
            print("Take this dumbass")
            print("""
            ....................../´¯/) 
            ....................,/¯../ 
            .................../..../ 
            ............./´¯/'...'/´¯¯`·¸ 
            ........../'/.../..../......./¨¯\ 
            ........('(...´...´.... ¯~/'...') 
            .........\.................'...../ 
            ..........''...\.......... _.·´ 
            ............\..............( 
            ..............\.............\...
            """)
            quit()
        else:
            print("Do you know English? Then why are doing this wrong? Try again!!")
            level_4alpha()


start()
