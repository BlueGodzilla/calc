def split(exp):
    exp = exp.replace('(', '( ')
    exp = exp.replace(')', ' )')
    exp = exp.replace('^', ' ^ ')
    exp = exp.split()

    return exp

def is_op(op):
    return op in ('+', '-', '/', '*', '^', '(', ')')

def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def lexer(exp):
    exp = split(exp)

    # check exp for valid syntax
    for op in exp:
        if not is_number(op) and not is_op(op):
            exit(f'Invalid operator/operand: \'{op}\'')

    for i in range(0, len(exp)):
        if is_number(exp[i]):
            exp[i] = float(exp[i])

    return exp

def parser(exp):

    try:

        i = 0
        
        while i < len(exp): # first cycle, ^
            if is_op(exp[i]):

                if i == 0: # Handle a bug with -1 list posiition
                    exit(f'\'{exp[i]}\' should go with two operands')

                if exp[i] == '^':
                    exp[i - 1] = pow(exp[i - 1], exp[i + 1])
                    del exp[i] # deleting unnecessary elements
                    del exp[i]
                    i = -1

            i += 1

        i = 0
        
        while i < len(exp): # second cycle, * and /
            if is_op(exp[i]):

                if i == 0: # Handle a bug with -1 list posiition
                    exit(f'\'{exp[i]}\' should go with two operands')

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

        while i < len(exp): # third cycle, + and -
            if is_op(exp[i]):

                if i == 0: # Handle a bug with -1 list posiition
                    exit(f'\'{exp[i]}\' should go with two operands')

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

    except TypeError:
        exit(f'Invalid arithmetic expression: \'{" ".join(str(x) for x in exp)}\'')
    except IndexError:
        exit(f'\'{exp[i]}\' should go with two operands')

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
                exit('Unfound open parenthesis')
            cpar = i
            try:
                exp[opar] = parser(exp[opar + 1:cpar])[0] # replacing open parenthesis with the result
                del exp[opar + 1:cpar + 1] # Deleting garbage
            except IndexError:
                exit('You should have something inside parentheses')
            i = -1

        i += 1

    if opar != -1 and cpar == -1:
        exit('Found unclosed open parenthesis')

    exp = parser(exp)
    return exp[0]