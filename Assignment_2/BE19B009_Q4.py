operators = ["(", "^", "/", "*", "+", "-", ")"]

def InfixToPostfix(infix):
    i = 0
    postfixStack = []
    operatorStack = []
    while i in range(len(infix)+1):
        number = ""
        try:
            while not infix[i] in operators:
                if(i < len(infix)):
                    number += infix[i]
                    i += 1
                else:
                    break

            if(number != ""):
                # print("A:", number)
                postfixStack.append(int(number))
                # else:

            if(infix[i]):
                # print(infix[i])
                if(len(postfixStack) == 0):
                    postfixStack.append(infix[i])
                elif(len(operatorStack) == 0):
                    operatorStack.append(infix[i])
                elif(infix[i] == "(" or infix[i] == "^"):
                    operatorStack.append(infix[i])
                elif(infix[i] == "*" or infix[i] == "/"):
                    if(len(operatorStack) != 0):
                        try:
                            while((operatorStack[-1] == "^" or operatorStack[-1] == "*" or operatorStack[-1] == "/")):
                                postfixStack.append(operatorStack.pop())
                            operatorStack.append(infix[i])
                        except:
                            operatorStack.append(infix[i])

                elif(infix[i] == "-" or infix[i] == "+"):
                    if(len(operatorStack) != 0):
                        try:
                            while((operatorStack[-1] == "+" or operatorStack[-1] == "-" or operatorStack[-1] == "/" or operatorStack[-1] == "*" or operatorStack[-1] == "^")):
                                postfixStack.append(operatorStack.pop())
                        except:
                            # print("hello")
                            operatorStack.append(infix[i])
                        

                elif(infix[i] == ")"):
                    if(len(operatorStack) != 0):
                        try:
                            while(len(operatorStack) != 0 and operatorStack[-1] != "("):
                                postfixStack.append(operatorStack.pop())
                            operatorStack.pop()
                        except:
                            operatorStack.pop()

                else:
                    postfixStack.append(infix[i])
        except:
            if(number != ""):
                # print("B:", number)
                postfixStack.append(int(number))
                if(len(operatorStack) != 0 ):
                        postfixStack.append(operatorStack.pop())

        i += 1
    return postfixStack

def EvaluatePostfix(postfix):

    evalStack = []
    for i in range(len(postfix)):
        if not postfix[i] in operators:
            evalStack.append(postfix[i])

        elif(postfix[i] == '+'):
            x = evalStack.pop()
            y = evalStack.pop()
            evalStack.append(y + x)
        
        elif(postfix[i] == '-'):
            x = evalStack.pop()
            y = evalStack.pop()
            evalStack.append(y - x)
        
        elif(postfix[i] == '*'):
            x = evalStack.pop()
            y = evalStack.pop()
            evalStack.append(y * x)
        
        elif(postfix[i] == '/'):
            x = evalStack.pop()
            y = evalStack.pop()
            evalStack.append(y / x)
        
        elif(postfix[i] == '^'):
            x = evalStack.pop()
            y = evalStack.pop()
            evalStack.append(y ** x)

    return evalStack.pop()


# postfix = InfixToPostfix("42+43/(55-66*72^32)+100-3")
postfix = InfixToPostfix("3^4/(5*6)+10")
print("Postfix expression: ", postfix)
answer = EvaluatePostfix(postfix)
print("Value of expression: ", answer)

