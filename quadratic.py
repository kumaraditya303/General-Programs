import os
def sign(x):
    if(x>=0):
        return "+"
    elif(x<0):
        return "-"
os.system("cls")
print("Quadratic solver:")
ax = int(input("Enter the coefficient of x\N{SUPERSCRIPT TWO}: "))
bx = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant: "))
if(abs(ax)==1 and abs(bx)==1):
    eq = "x\N{SUPERSCRIPT TWO} " + sign(bx)+" x "+sign(c) + str(abs(c))+" = 0"
else:
    eq = str(ax)+"x\N{SUPERSCRIPT TWO} "+sign(bx)+str(abs(bx))+"x "+sign(c) + str(abs(c))+" = 0"
os.system("cls")
print("Quadratic solver:")
print("Equation: "+eq)
pans = (-bx+(bx**2-4*ax*c)**(1/2))/(2*ax)
nans = (-bx-(bx**2-4*ax*c)**(1/2))/(2*ax)
pans = str(pans).replace("j", "i")
nans = str(nans).replace("j", "i")
print("First solution: "+pans)
print("Second solution: "+nans)
