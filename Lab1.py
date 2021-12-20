#Zachary Koontz
#Propositional Logic truth table generator Lab
#Intended Rubric = R3

import itertools
import sys

def menu():
    print("Propositional Logic Program and Truth table generator")
    print("****************************************************")
    print("1. Create a Truth Table")
    print ("2. Exit")
    choice = input("Please select an option")
    if choice == "1":
        truth_table()
    elif choice =="2":
        print("Program Terminated")
        sys.exit()
    else:
        print("That is an Invalid option")
        menu()

def truth_table():
    while True:
        try:
            inps = int(input(
                "Please enter the number of inputs you want 1-5, when truth table is generated, A = the ending truth values for the truth table"))
            if inps <1 or inps>5:
                print ("1 input min, 5 max")
            else:
                break
        except:
            ValueError
            print("You must input a number between 1 and 5")

    truths = list(itertools.product([True,False], repeat=inps))

    statement = input("Please input the Propsitional Logic statement")
    statement = statement.lower()

    print("P and Q or R")
    print("P\t '    ' \tQ\t '    ' \tR\t '    ' \tA\t")
    print("-"*20*inps)

    for item in truths:
        pos = 0
        if inps ==1:
            p = item[0]
        elif inps ==2:
            p,q = item[0],item[1]
        elif inps ==3:
            p,q,r = item[0],item[1],item[2]
        elif inps ==4:
            p,q,r,a = item[0],item[1],item[2],item[3]
        else:
            p,q,r,a = item[0],item[1],item[2],item[3]
            pos = 0
        while pos < inps:
            print (item[pos],end = "\t\t")
            pos +=1
        try:
            truth = eval(statement)
            print (truth)
        except:
            print("Not a valid response, please check input")
    print ()
    wait = input("Press the eneter button to go back to the Menu")
    menu()

menu()
