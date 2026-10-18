x=int(input("Enter your first number:"))
y=int(input("Enter your second number:"))
z=input("Enter your function(+,-,*,/):")


def addition(x,y):
    print(x+y)
def subtraction(x,y):
    print(x-y)
def multiplication(x,y):
    print(x*y)
def division(x,y):
    if y!=0:
        print(x/y)
    elif y==0:
        print("The integer cannot be divided by zero")
        
        
        
if z== "+":
    addition(x,y)
elif z=="-":
    if x>y:
        subtraction(x,y)
    elif x<y:
        subtraction(y,x)
elif z=="*":
    multiplication(x,y)
elif z=="/":
     if y!=0:
         print(x,y)
     elif y==0:
         print("The integer cannot be divided by zero")

else:
    print("Invalid function")