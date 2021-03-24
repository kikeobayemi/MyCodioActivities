#Write a program that takes a list called my_list (it could be a list of any data type) 
#and prints the list three times if the length of the list is less than 5. 
#If the length of my_list is greater than or equal to 5, then print the list one time.
#code will be automatically tested with two lists: my_list = ['hi', 'hello'] and my_list = [65, 111, 2, 81, 65, 32]

########################################################
# DO NOT EDIT THE CODE IN THE SECTION BELOW
########################################################
import sys

my_list = sys.argv[1:]

########################################################
# Enter your code below
########################################################
length=len(my_list)
if length < 5:
  print(my_list *3)
else:
  print(my_list)