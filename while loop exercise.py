#Using while True:, create a loop that prints the sum of all the numbers between 0 and 100. 
#Note: the sum should include the number 100.

#mycode
#sum1 = 0
#counter = 1
#while True:
 
 # sum1 = sum1 + counter
  #counter = counter + 1
  #print(sum1)
  #if counter == 100:
   # break
total = 0
count = 0
while True:
  if count > 100:
    break
  else:
    total = total + count
    count += 1
print(total)