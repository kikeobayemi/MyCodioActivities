#Problem
#Write a program that takes a list called numbers that has an even length. 
#Your program should should insert an '*' between each element of the list. 
#Then print the modified list.
########################################################
# Erase the variable numbers before submitting your work
########################################################

numbers = [0,0,0,0,0,0]

########################################################
# Enter your code below
########################################################
length = len(numbers)+len(numbers)-1
for i in range(1,length,2):
    numbers.insert(i, "*")
print(numbers)