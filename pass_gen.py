import random

chars = "abcdefghijklmnopqrstupwxyzABCDEFGHIJKLMNOPQRSTUPWXYZ`1234567890-=+_)(*&^%$#@!~[]\;',./{}|:<>?"

password_len = int(input("How many letters will would you like your password to contain?: "))
password_count = int(input("How many password should I generate?: "))


for x in range(0, password_count):
    password = ""
    for x in range(0, password_len):
        password_char = random.choice(chars)
        password = password + password_char
    print("Your password is: " + password)
