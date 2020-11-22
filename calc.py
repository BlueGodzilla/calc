def split(exp):
    exp = exp.replace('(', '( ')
    exp = exp.replace(')', ' )')
    exp = exp.split()

    return exp

def is_op(op):
    return op in ('+', '-', '/', '*', '(', ')')

def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def parser(exp):
    exp = split(exp)

    # check exp for valid syntax
    for op in exp:
        if not is_number(op) and not is_op(op):
            exit('Invalid Syntax')

    for i in range(0, len(exp)):
        if is_number(exp[i]):
            exp[i] = float(exp[i])

    return exp

def evaluate(exp):

    i = 0
    
    while i < len(exp): # first cycle, * and /
        if is_op(exp[i]):

            if i == 0 or i == len(exp) - 1: # check if an operator is the last/first element
                exit('Invalid Syntax')

            if exp[i] == '*':
                exp[i - 1] = exp[i - 1] * exp[i + 1]
                del exp[i] # deleting unnecessary elements
                del exp[i]
                i = -1
            elif exp[i] == '/':
                exp[i - 1] = exp[i - 1] / exp[i + 1]
                del exp[i]
                del exp[i]
                i = -1

        i += 1

    # TODO: *maybe* improve this copypaste

    i = 0

    while i < len(exp): # second cycle, + and -
        if is_op(exp[i]):

            if i == 0 or i == len(exp) - 1: # check if an operator is the last/first element
                exit('Invalid Syntax')

            if exp[i] == '+':
                exp[i - 1] = exp[i - 1] + exp[i + 1]
                del exp[i] # deleting unnecessary elements
                del exp[i]
                i = -1
            elif exp[i] == '-':
                exp[i - 1] = exp[i - 1] - exp[i + 1]
                del exp[i]
                del exp[i]
                i = -1

        i += 1



    return exp

def calc(exp):

    opar = -1 # position of open parentheses
    cpar = -1 # position of close parentheses

    i = 0 # counter

    while i < len(exp):

        if exp[i] == '(':
            opar = i
        elif exp[i] == ')':
            if opar == -1:
                exit('Invalid Syntax') # I'm not checking for existence of a close parenthesis 'cause the `evaluate` function will do it 
            cpar = i
            exp[opar] = evaluate(exp[opar + 1:cpar])[0] # replacing open parenthesis with the result
            del exp[opar + 1:cpar + 1] # Deleting garbage
            i = -1

        i += 1

    exp = evaluate(exp)
    return exp[0]