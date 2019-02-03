import math
import sys

def Calc(term):
    term = term.replace(' ', '')
    term = term.replace('?', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('rad', 'radians')
    term = term.replace('%', '/100')
    term = term.replace('mod', '%')

    functions = ['sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 'sqrt', 'radians', 'pi', 'e']

    term = term.lower()

    for func in functions:
        if func in term:
            withmath = 'math.' + func
            term = term.replace(func, withmath)

    try:
        term = eval(term)

    except AttributeError:
        print("Invalid Usage")

    except NameError:
        print("Check again")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    return term

def result(term):
    print(str(Calc(term)))

def main():
    print("Scientific Calculator \n\n Type Exit to quit")

    if sys.version_info.major >= 3:
        while True:
            k = input("What is? ")
            if k == 'Exit':
                break
            result(k)

    else:
        while True:
            k = input("What is? ")
            if k == 'Exit':
                break
            result(k)

if __name__ == '__main__':
    main()
