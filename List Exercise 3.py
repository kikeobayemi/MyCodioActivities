#Write a program that takes a list called strings that contains a random selection of strings. 
#Your program should print the first string when arranged in alphabetical order.
#code will be automatically tested with two lists: strings = ['luck', 'cat', 'kid', 'house'] and
#strings = ['duck', 'dddd', 'mouse', 'kite']

########################################################
# DO NOT EDIT THE CODE IN THE SECTION BELOW
########################################################
import sys

strings = sys.argv[1:]

########################################################
# Enter your code below
########################################################
strings.sort()
print(strings[0])