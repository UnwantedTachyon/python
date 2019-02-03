import random

upper = random.randint(1, 20)
lower = random.randint(21, 6552)

print("Primes between", upper, "and", lower, "are: ")

for num in range(upper, lower + 1):
    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                break

        else:
            print(num)