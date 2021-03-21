#Problem
#Use the variable x as you write this program. x will represent a string. 
#Write a program using the elif keyword that determines if x is a primary color (red, blue, or yellow). 
#If yes, print _ is primary color, where the blank is the value of x. 
#If no, print _ is not a primary color, where the blank is the value of x.


x = "cyan"
if x == "red":
  print(x + " is a primary color ")
elif x == "blue":
  print(x + " is a primary color ")
elif x == "yellow":
  print(x + " is a primary color ")
else:
  print(x + " is not a primary color")