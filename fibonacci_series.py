a=int(input("Enter first number of the series: "))
b=int(input("Enter second number of the series: "))
n=int(input("Number of elements: "))
print(a,b, end = " ")
for i in range(1,n-1):
    c = (a+b)
    a=b
    b=c
    print(c, end=" ")
    n=n-1
