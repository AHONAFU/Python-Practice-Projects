import time

print('''
########  ########     ########  ####  ######  ######## ########  ####  ######  ########  ######  
##     ## ##     ##    ##     ##  ##  ##    ##    ##    ##     ##  ##  ##    ##    ##    ##    ## 
##     ## ##     ##    ##     ##  ##  ##          ##    ##     ##  ##  ##          ##    ##       
########  ##     ##    ##     ##  ##   ######     ##    ########   ##  ##          ##     ######  
##     ## ##     ##    ##     ##  ##        ##    ##    ##   ##    ##  ##          ##          ## 
##     ## ##     ##    ##     ##  ##  ##    ##    ##    ##    ##   ##  ##    ##    ##    ##    ## 
########  ########     ########  ####  ######     ##    ##     ## ####  ######     ##     ######  

''')

print("##### If you want to quit just type 'quit' #####")

districts = ["Dhaka", "Faridpur", "Gazipur", "Gopalganj", "Jamalpur", "Kishoreganj", "Madaripur", "Manikganj",
             "Munshiganj", "Mymensingh", "Narayanganj", "Narsingdi", "Netrakona", "Rajbari", "Shariatpur", "Sherpur",
             "Tangail", "Bogura", "Joypurhat", "Naogaon", "Natore", "Chapainawabganj", "Pabna", "Rajshahi", "Sirajganj",
             "Bandarban", "Brahmanbaria", "Chandpur", "Chattogram", "Cumilla", "Cox's Bazar", "Feni", "Khagrachari",
             "Lakshmipur", "Noakhali", "Rangamati",
             "Bagerhat", "Chuadanga", "Jessore", "Jhenaidah", "Khulna", "Kushtia", "Magura", "Meherpur", "Narail",
             "Satkhira",
             "Barguna", "Barishal", "Bhola", "Jhalokati", "Patuakhali", "Pirojpur",
             "Habiganj", "Moulvibazar", "Sunamganj", "Sylhet",
             "Dinajpur", "Gaibandha", "Kurigram", "Lalmonirhat", "Nilphamari", "Panchagarh", "Rangpur", "Thakurgaon"]

converted_list = [x.upper() for x in districts]

def timer(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


def game():
    ans = input("Guess the district: ")
    ans = ans.upper()

    if ans in converted_list:
        converted_list.remove(ans)
        remainer = len(converted_list)
        print(str(remainer) + " districts left")
        if remainer == 0:
            end_time = time.time()
            time_lapsed = end_time - start_time
            timer(time_lapsed)

            print("Congrats !!!! You have successfully named all the districts of Bangladesh .")
            
        game()

    elif ans == "QUIT":
        remainer = len(converted_list)
        end_time = time.time()
        time_lapsed = end_time - start_time
        timer(time_lapsed)
        print("You've answered " + str(64-int(remainer)) + " districts. " + str(remainer) + " districts left")
        print(converted_list)
        input(":")
    else:
        remainer = len(converted_list)
        print("Not a district. " + str(remainer) + " districts left")
        game()

start_time = time.time()
game()


					
