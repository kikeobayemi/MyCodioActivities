#Write a program that takes a list of integers called numbers and replaces each element greater than 10 with a '*'. 
#Print the new version of numbers.
#Code will be automatically tested with the list: numbers = [30, 1, 20, 4].


import sys

numbers = sys.argv[1:]
for i in range(len(numbers)):
  numbers[i] = int(numbers[i])

########################################################
# Enter your code below
########################################################
numbers_1=[]
for number in numbers:
  if number>10:
    numbers_1.append("*")
  else:
    numbers_1.append(number)
print(numbers_1)