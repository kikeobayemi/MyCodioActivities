#Problem
#Write a program that takes input from a user. Print the first half of the string on one line, 
#and the second half on another. In the case of a string that has an odd number of characters, 
#the second line will have the extra character. Important, do not put a prompt when asking for user input. 
#Just use input(). Adding a prompt will cause your program to not pass the tests.
text=input()
string1 = text[0:len(text)//2]
string2 = text[len(text)//2:len(text)]
print(string1)
print(string2)