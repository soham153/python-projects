def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

opertations={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    num1 = int(input("enter first number: "))

    flag = True
    while(flag):
        for i in opertations:
            print(i)
        perform = input("enter operation to be performed: ")
        num2 = int(input("enter second number: "))

        result = opertations[perform](num1,num2)
        print(f"{num1} {perform} {num2} = {result}")


        print("type Y to continue , N to stop and E to exit")
        continue_or_not = input()

        if(continue_or_not == "Y" or continue_or_not == "y" ):
            num1 = result
            
        if(continue_or_not == "N" or continue_or_not == "n"):
            flag = False
            print("\n"*15)
            calculator()
            
calculator()
