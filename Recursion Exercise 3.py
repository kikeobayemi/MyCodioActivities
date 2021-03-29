def bunny_ears(num1):
  "Calculate the total number of ears of the bunnies specified using num1 "
  if num1 == 0:
    return 0
  else:
    return 2 + bunny_ears(num1-1)
  
bunny_ears(8)