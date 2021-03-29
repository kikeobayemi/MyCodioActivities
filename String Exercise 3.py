#Write a program that accepts input from the user. 
#Create another string that contains either a u, l, or - for each character of the original string. 
#Use u when the character is uppercase, and use l when the character is lowercase. 
#If the character is neither uppercase or lowercase, use -. 
#Print the second string. Important, do not put a prompt when asking for user input. 
#Just use input(). Adding a prompt will cause your program to not pass the tests.
text=input()
my_string=""
for char in text:
  if char.isupper():
    my_string+="u"
  elif char.islower():
    my_string+="l"
  else:
    my_string+="-"
print(my_string)