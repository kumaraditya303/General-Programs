file = open("num.txt","w")

x = int(input("Enter a number= "))
y = 1
for i in range(1,11,1):
    w=str(x) +" * "+str(i) +" = "+str(x*i)
    print (w)
    file.write(w+"\n")
    
for j in range(1,x+1,1):
    y*=j
print("It's factorial = "+ str(y))
file.close()