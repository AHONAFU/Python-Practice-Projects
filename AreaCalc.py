print('''                             _____      _            _       _             
     /\                     / ____|    | |          | |     | |            
    /  \   _ __ ___  __ _  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   / /\ \ | '__/ _ \/ _` | | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  / ____ \| | |  __/ (_| | | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 /_/    \_\_|  \___|\__,_|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                           
                                                                           ''')

print('''Select---             Sqare/Rhombus       Rectangle/Parallelogram     Circle


Cube                Cylinder                    Triangle


             #The script is case sensative so type as it is above''')
print()
print()

shape1 = "Sqare"
shape2 = "Rectangle"
shape3 = "Circle"
shape4 = "Cube"
shape5 = "Cylinder"
shape6 = "Triangle"
shape11 = "Rhombus"
shape12 = "Parallelogram"

shape_input = str(input("Enter the name of your shape: "))

if shape_input == shape1:
    a = float(input("Enter the length of 1 side: "))
    area = a * a
    print()
    print("The area of your " + shape_input + " is: " + str(area))

elif shape_input == shape11:
    a = float(input("Enter the length of 1 side: "))
    area = a * a
    print()
    print("The area of your " + shape_input + " is: " + str(area))

elif shape_input == shape2:
    a = float(input("Enter the height: "))
    b = float(input("Enter the width: "))
    area = a * b
    print()
    print("The are of your " + shape_input + " is: " + str(area))

elif shape_input == shape12:
    a = float(input("Enter the height: "))
    b = float(input("Enter the width: "))
    area = a * b
    print()
    print("The area of your " + shape_input + " is: " + str(area))

elif shape_input == shape3:
    a = float(input("Enter the radius: "))
    area = 3.1416 * (a * a)
    print("The are of your Circle is: " + str(area))

elif shape_input == shape4:
    a = float(input("Enter the length of 1 side: "))
    area = a * a * a
    print("The area of your Cube is: " + str(area))

elif shape_input == shape5:
    r = float(input("Enter the radius: "))
    h = float(input("Enter the height: "))
    area = (2 * 3.1416 * r * h) + (2 * 3.1416 * (r * r))
    print("The area of your Cylinder is : " + str(area))

elif shape_input == shape6:
    b = float(input("Enter the base: "))
    h = float(input("Enter the height: "))
    area = 0.5 * b * h
    print("The area of your Triangle is: " + str(area))

else:
    print("I don't think that's in the list. Please check your spelling.")





