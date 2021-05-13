postStack = []                          #lists used to create stacks
inStack = []
postfix = []

def opCheck(x) :                        #Checks to see if a value is an operand (Not + - / * ( or ))
	return ((x >= 'a' and x <= 'z') or 
            (x >= 'A' and x <= 'Z') or
            (x >= '0'))

def pushStack(notation) :
	
	for i in notation:
		inStack.append(i)     #Simple method to create the infix stack

def algo(InfixStack):
    for i in InfixStack:          #for each value in the stack
        if (opCheck(i)):            #if operand, push into the postfix stack
            postfix.append(i)
        elif (i in '('):                   #else check if in paranthesis
            postStack.insert(0, i)
        elif (i in ')'):
            while (postStack[0] is not '('):
                postfix.append(postStack[0])
                postStack.pop(0)
            postStack.pop(0)
        if (i in '*/+-'):                               #Checks if which operator and it's heirarchy
            if (len(postStack) == 0):
                postStack.insert(0,i)
            elif(i in'/*' and postStack[0] in '/*'):
                postfix.append(postStack[0])
                postStack.pop(0)
                postStack.insert(0,i)
            elif(i in'+-' and postStack[0] not in '+-/*'):
                postStack.insert(0, i)
            elif(i in '+-' and postStack[0] in '+-*/'):
                postfix.append(postStack[0])
                postStack.pop(0)
                postStack.insert(0,i)
            elif(i in '/*' and postStack[0] not in '/*'):
                postStack.insert(0, i)
    postfix.append(postStack[0])                    #Append and pop the final operator
    postStack.pop(0)                            
        


if __name__ == '__main__':

	notation = "(A+(B*C))-((D/E)*F)".replace(' ', '') #Beginning infix notation

pushStack(notation)     #Push the postfix notation onto a stack
algo(inStack)         #Algorithm to change the infix to postfix
poststring = ''
for i in postfix:        #Converts list into string
    poststring += i
print('The infix notation is: ' + notation)
print('The postfix notation is: ' + poststring)       #Prints the remaining string after the algorithm is complete
