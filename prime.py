print("Prime Number Printer:")
x=int(input("Enter Lower Range = "))
y=int(input("Enter Higher Range = "))
y+=1
z=0
if (y<x):
    y-=1
    x+=1
    a=x
    x=y
    y=a
for num in range(x,y,1):
    if num>0:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else: 
            print(num)
            z+=1
print("Number of Prime Numbers Between "+str(x)+" and "+str(y-1)+" are = "+str(z))