#Write a program that captures text from the user. Print the user string as many times as its length. 
#Print as many lines of this as the length of the user input. Important, do not put a prompt when asking for user input. 
#Just use input(). Adding a prompt will cause your program to not pass the tests.
text=input()
my_string = text * len(text)
for i in range(len(text)):
  print(my_string)