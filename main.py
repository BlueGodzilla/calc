from sys import argv
import calc

if len(argv) == 1:
    exit('(no expression)')

exp = calc.parser(argv[1])

exp = calc.calc(exp)

print(exp)