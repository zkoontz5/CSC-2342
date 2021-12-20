#Zach Koontz
#Sequence Generator
#Intended Rubric = A (All tasks Completed)

a1 = int(input("Enter the first term of the sequence (a1): "))
number_of_terms = int(input("Enter the number of terms in the sequence: "))
generator = input("Enter the rule generator (Must enter with an N, ex: 3n-1): ")

lst = generator.split('n')
d = int(lst[0])

an = a1+((number_of_terms-1)*d)
x = 0

for i in range(a1, an+1, d):
   print(x+a1)
   x += d
