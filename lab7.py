import math

def main():

    o = input("Does order of output values matter? Enter y for yes and n for no: ")
    sum = 1
    product = 2

    if o == 'n' or o == 'N':
        n = int(input("How many sets will you be inputing?: "))
        for i in range(0,n):
            set = input("Enter set (Use commas to seperate): ")
            element = set.split(",")
            sum += len(element)
            product += len(element)
    elif o == 'y' or o == 'Y':
        set1 = input("Enter all elements of the set (n) seperated by commas: ")
        element2 = set1.split(",")
        sub = int(input("Enter the size of the subset(r): "))

        sum = len(element2) + sub
        if sub == 0:
            product = math.factorial(len(element2))
        elif sub != 0:
            product = (math.factorial(len(element2))) / (math.factorial(len(element2) - sub))

    print("Using the Sum Rule: ", sum)
    print("Using the Product Rule: ", product)

if __name__=='__main__':
    main()
