import random
import time
x = "yes"
while x == "yes":
    for i in range(0, 1):
        a = random.randint(30, 99)
        b = input("Your name: ")
        c = input("Your Crush's Name: ")

        print("calculating....")
        time.sleep(2)
        print(".................")
        time.sleep(1) 
        print("...")
        time.sleep(0.5)
        print("Connection between", b, "and", c, "is", a, "% strong")

    x = input("wanna try again? ")
        