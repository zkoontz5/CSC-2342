#Zach Koontz
#Prime and Composite - Lab 5
#Rubric - A(All Tasks completed)

number = int(input("Enter a positive integer: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is a composite number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is a composite number")
