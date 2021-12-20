#Zach Koontz
#Set Evaluator - Lab 3
#Intended Rubric = A (All tasks Completed)

import random
import string


def one_to_one(d_set, r_set):
    st = set()
    if (len(r_set) >= len(d_set)):
        for (i, j) in zip(d_set, r_set):
            st.add((i, j))
        print(
            '************************************************one-to-one functions of the given set*****************************************')
        print("f : ", end='')
        for i in st:
            for j in i:
                if ("<class 'int'>" == str(type(j))):
                    number = j
                else:
                    char = j
            print(number, "->", char, ",\t", end='')
    else:
        print(
            "\nThere will be no one-to-one function\nAs we know that if the number of elements of the Set A is greater than the number of elements pf the Set B - then there will be no one to one function ")
        print('A= ', d_set)
        print('B= ', r_set)


def onto(d_set, r_set):
    st = set()

    if (len(d_set) >= len(r_set)):

        lst = list(r_set)
        count = 0
        for i in d_set:
            if (count < len(r_set)):

                st.add((i, lst[count]))
                count += 1

                if (count == len(r_set)):
                    count = 0

        print("*********************onto functions of the given sets*******************")
        print("f : ", end='')

        for i in st:
            for j in i:
                if ("<class 'int'>" == str(type(j))):
                    number = j
                else:
                    char = j
            print(number, "->", char, ",\t", end='')

    else:
        print('The number of onto function=0')


x = int(input("Enter 1 to start the program : Program for Evaluating Sets:\t"))
bl = True
while (bl):
    if (x == 1):
        n1 = int(input('Enter the number of elements for the character set: '))

        d_set = set()
        r_set = set()
        for i in range(n1):
            i = input('Enter the character element for the set')
            d_set.add(i)
        n2 = int(input('Enter the number of elements for the number set: '))
        for j in range(n2):
            j = int(input('Enter the number elemnet for the set'))
            r_set.add(j)

    print("1. One-to-One")
    print("2. Onto")

    option = int(input("Enter your choice:\t"))

    if (option == 1):
        one_to_one(d_set, r_set)

    elif (option == 2):
        onto(d_set, r_set)

    else:
        print("Invalid choice")

    ch = input("\nEnter Q for quit or any other character to enter another pair of sets:\t")
    if (ch == 'q' or ch == 'Q'):
        bl = False
