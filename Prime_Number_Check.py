x = "y"
while x == "y":
    num = int(input("Number to check? "))

    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                print(num, "is not a prime number.")
                print(i, "times", num//i, "is", num, ".")
                break

        else:
            print(num, "is a prime number.")

    else:
        print(num, "is a prime number.")

    x = input("Want to try again(y/n)? ")

             