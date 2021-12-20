import math
import random


def coinToss():
    number = int(input("How many times should the coin should be flipped?: "))
    heads_number = int(input("How many of these flips should come up as heads?: "))
    recordList = []
    heads = 0
    tails = 0
    for amount in range(number):
        flip = random.randint(0, 1)
        if (flip == 0):
            recordList.append("Heads")
        elif (flip == 1):
            recordList.append("Tails")

    probability_of_heads1 = math.factorial(number) / (
                math.factorial(heads_number) * math.factorial(number - heads_number))
    probability_of_heads2 = (2) ** number
    probability_of_heads3 = math.factorial(number) / (
                math.factorial(heads_number) * math.factorial(number - heads_number)) * ((1 / 2) ** number)

    print(recordList)
    print('\nThe probability of', heads_number, "heads in", number, "times flipping the coin is",
          int(probability_of_heads1), "/", probability_of_heads2, " which is also {:.2f}".format(probability_of_heads3 * 100),
          "%")


coinToss()
