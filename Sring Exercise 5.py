#Write a program that captures input from the user. Then, swap the letters two at a time in the string. 
#The first two characters change places, the third and fourth characters change places, etc. 
#Assume that the user will only input strings with an even number of characters. 
#Important, do not put a prompt when asking for user input. Just use input(). 
#Adding a prompt will cause your program to not pass the tests.
text=input()
index = 0
temp=0
my_string=""
while index < len(text)-1:
  x=text[index]
  y=text[index+1]
  temp=x
  x = y
  y=temp
  my_string+=("{}{}").format(x,y)
  index+=2
print(my_string)