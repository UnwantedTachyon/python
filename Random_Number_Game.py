import random

x = "y"
while x == "y":
    for i in range(0, 5):
        a = random.randint(1, 20)
        b = int(input("\nYour guess: "))

        if a == b:
            print(a)
            print("you win")
            break

        if b>20:
            print("Check range") 
        
        if i == 5:
            print("you loose")
            break

        if a!=b:
            print(a)
            print("Wrong guess") 
    
    x = input("Try agian(y/n): ")            