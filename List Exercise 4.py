Problem
#Write a program that takes a list called numbers that contains integers in a sequence 
#(the sequence is always increasing, never decreasing). 
#Your program should add the next two numbers in the sequence, and then print the list.
########################################################
# Erase the variable numbers before submitting your work
########################################################

numbers = [-5,-4,-3,-2]

########################################################
# Enter your code below
########################################################
length = numbers.pop()
for i in range(3):
  numbers.append(length+i)
print(numbers)