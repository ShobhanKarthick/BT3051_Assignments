operators = ["(", "^", "/", "*", "+", "-", ")"]
postfixStack = []
operatorStack = []

def InfixToPostfix(infix):
    i = 0
    while (i <= len(infix)):
        number = ""
        j = i 
        while(j < len(infix)):
            if (infix[j] not in operators):
                number += infix[j]
                j += 1
            else:
                break

        if (number != ""):
            if(len(operatorStack) == 0):
                postfixStack.append(number)
            
            print(number)
        i = j+1
        try:
            if(len(operatorStack) == 0):
                postfixStack.append(infix[i-1])
            else:
                operatorStack.append(infix[i-1])
            print(infix[i-1])
        except:
            break

InfixToPostfix("32^43/(55*66+72)+10")
print(operatorStack)
print(postfixStack)



    
