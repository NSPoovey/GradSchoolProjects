postStack = []
inStack = []

def opCheck(x) :                        #Checks to see if a value is an operand (Not + - / or *)
	return ((x >= 'a' and x <= 'z') or 
            (x >= 'A' and x <= 'Z') or
            (x >= '0'))

def pushStack(notation) :
	
	for i in notation:
		postStack.append(i)     #Simple method to create the postfix stack


def algo(PostfixStack):
    
    for i in PostfixStack:          #for each value in the stack

        if (opCheck(i)):            #if operand, push into the infix stack
            inStack.insert(0,i)
        else:                       #else pop the top two operands
            operand1 = inStack[0]
            inStack.pop(0)
            operand2 = inStack[0]
            inStack.pop(0)
            inStack.insert(0, "(" + operand2 + i + operand1 + ")")   #place the operator in between and encapsulate in parenthesis

if __name__ == '__main__':

	notation = "A B C * + D E / F * -".replace(' ', '') #Beginning postfix notation

pushStack(notation)     #Push the postfix notation onto a stack
algo(postStack)         #Algorithm to change the postfix into infix
print('The postfix is: ' + notation)
print('The infix is : ' + inStack[0])       #Prints the remaining string after the algorithm is complete
