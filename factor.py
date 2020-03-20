x = int(input("Enter A Number = "))
y = 0
if x > 1:
    for i in range(1, x+1, 1):
        if (x % i) == 0:
            print("Factor = ", str(i))
            y += 1
    if y == 2:
        print(str(x)+" is a Prime Number.")
    else:
        print("Number of Factors of "+str(x)+" = "+str(y)+".")
if x == 0:
    print("You entered 0.")
if x == -1:
    print("-1 is a Unique Number.")
if x == 1:
    print("1 is a Unique Number.")
if x < -1:
    for i in range(-1, x-1, -1):
        if (x % i) == 0:
            print("Factor = ", str(i))
            y += 1
    if y == 2:
        print(str(x)+" is a Prime Number.")
    else:
        print("Number of Factors of "+str(x)+" = "+str(y)+".")
