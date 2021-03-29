#Problem
#Write a program that takes input from a user and prints the first character of the input 
#and the last character with some context. Important, do not put a prompt when asking for user input. 
#Just use input(). Adding a prompt will cause your program to not pass the tests.

text = input()
fir=text[0]
las=text[len(text)-1]
string1 = ("{} is the first character and {} is the last character").format(fir,las)
print(string1)