#Zachary Koontz
#Email: zkoontz@highpoint.edu
#Predicate Logic Quantifier
#Intended Rubric = R3

import operator as o


def QuantifyPredicates():
    print("--- choose a predicate variable type --- ")
    print("1. Unary")
    print("2. Binary")
    print("3. Ternary")

    choice = input()
    if choice == "1":
        QuantifyUnaryVariable()

    elif choice == '2':
        QuantifyBinaryVariable()

    elif choice == "3":
        QuantifyTernaryVariable()

    else:
        print("Invalid Input")


def QuantifyUnaryVariable():
    operators = {'1': o.gt, '2': o.lt, '3': o.eq, '4': o.ne}

    print("--- choose type of function you want to perform on unary predicate --- ")
    print("1. x > 2")
    print("2. x < 2")
    print("3. x == 2")
    print("4. x != 2")

    op = input()

    print("--- Enter domain values for the predicate variable --- ")
    i_domain = int(input("initial value: "))
    f_domain = int(input("final vlaue: "))
    print("X=[", i_domain, ",", f_domain, "]")

    print("--- Enter quantifier type you want to perform on predicate variable --- ")
    quantifier = input("choose U/E: ")
    count = 0
    op = operators.get(op)

    if quantifier == 'e' or quantifier == "E":

        for i in range(i_domain, f_domain + 1):
            if op(i, 2):
                count = count + 1

        if (count > 0):
            print("\nT")
        else:
            print("\nF")

    if quantifier == 'u' or quantifier == "U":
        for i in range(i_domain, f_domain + 1):
            if op(i, 2):
                count = count + 1

        if count == (f_domain - i_domain + 1):
            print("\nT")
        else:
            print("\nF")


def QuantifyBinaryVariable():
    operators = {'1': o.gt, '2': o.lt, '3': o.add, '4': o.add}

    print("--- choose type of function you want to perform on Binary predicate --- ")
    print("1. x > y")
    print("2. x < y")
    print("3. x == y")
    print("4. x != y ")

    op = input()

    print("\n--- Enter domain values for the predicate variables X and Y --- \n")
    i_domainX = int(input("Initial domain value for 'X': "))
    f_domainX = int(input("Final domain vlaue for 'X': "))

    i_domainY = int(input("Initial domain value for 'Y': "))
    f_domainY = int(input("final domain vlaue for 'Y': "))
    print("X=[", i_domainX, ",", f_domainX, "]", end=" ")
    print(" Y=[", i_domainY, ",", f_domainY, "]")

    print("--- Enter quantifier type you want to perform on predicate variable --- ")
    quantifier = input("Choose U/E: ")
    count = 0
    op = operators.get(op)

    if quantifier == 'e' or quantifier == "E":

        for i in range(i_domainX, f_domainX + 1):
            for j in range(i_domainY, f_domainY + 1):
                if op(i, j):
                    count = count + 1
                    break
            if count > 0:
                break

        if (count > 0):
            print("\nT")
        else:
            print("\nF")

    if quantifier == 'u' or quantifier == "U":
        for i in range(i_domainX, f_domainX + 1):
            for j in range(i_domainY, f_domainY + 1):
                if op(i, j):
                    count = count + 1

        if count == ((f_domainX - i_domainX + 1) * (f_domainY - i_domainY + 1)):
            print("\nT")
        else:
            print("\nF")


def QuantifyTernaryVariable():
    operators = {'1': [o.add, o.gt], '2': [o.sub, o.gt], '3': [o.add, o.lt], '4': [o.sub, o.lt]}
    print("--- choose type of function you want to perform on Ternary predicate --- ")
    print("1. x + y > z")
    print("2. x - y > z")
    print("3. x + y < z")
    print("4. x - y < z")

    op = input()
    i_domainX = int(input("Initial domain value for 'X': "))
    f_domainX = int(input("Final domain value for 'X': "))

    i_domainY = int(input("Initial domain value for 'Y': "))
    f_domainY = int(input("Final domain value for 'Y': "))

    i_domainZ = int(input("Initial domain value for 'Z': "))
    f_domainZ = int(input("Final domain value for 'Z': "))

    print("X=[", i_domainX, ",", f_domainX, "]", end=" ")
    print(", Y=[", i_domainY, ",", f_domainY, "]", end=" ")
    print(", Z=[", i_domainZ, ",", f_domainZ, "]")

    print("--- Enter quantifier type you want to perform on predicate variable --- ")
    quantifier = input("Choose U/E: ")
    count = 0
    op1 = operators[op][0]
    op2 = operators[op][1]

    if quantifier == 'e' or quantifier == "E":

        for i in range(i_domainX, f_domainX + 1):
            for j in range(i_domainY, f_domainY + 1):
                for k in range(i_domainZ, f_domainZ + 1):
                    leftExp = op1(i, j)
                    if op2(leftExp, k):
                        count = count + 1
                    break

                if count > 0:
                    break

        if (count > 0):
            print("\nT")
        else:
            print("\nF")

    elif quantifier == 'u' or quantifier == "U":
        for i in range(i_domainX, f_domainX + 1):
            for j in range(i_domainY, f_domainY + 1):
                for k in range(i_domainZ, i_domainZ + 1):
                    leftExp = op1(i, j)
                    if op2(leftExp, k):
                        count = count + 1

        if count == ((f_domainX - i_domainX + 1) * (f_domainY - i_domainY + 1)):
            print("\nT")
        else:
            print("\nF")


if __name__ == '__main__':
    message = '''welcome!!
               Before starting please do follow the instructions given below
               This program outputs the truth or False value after quantifying the predicates
               1-predicates are unary(X), binary(X,Y) or ternary(X,Y,Z), hence you must choose from the given list of predicate variables
                   1. Unary
                   2. Binary
                   3. Ternary
                   user inputs "1", then "Unary will be selected"

               2-The functions for the specific predicates will be listed on the screen, you must choose from them only

               3-You will be asked for domain values of predicate variables, you must enter integer values for domain
                   Note: domain values are inclusive from both the sides

               4-you need to enter type of quantifier for qunatifying the predicate variable.
                    :Enter u/U for using Universal Quantifier, e/E for Existential Quantifier'''
    print(message)
    QuantifyPredicates()
