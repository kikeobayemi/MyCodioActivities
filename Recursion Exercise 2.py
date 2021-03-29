def list_sum(list1):
  """Calculates the sum of all numbers in list1"""
 
  if len(list1) == 1:
    return list1[0]
  else:
    return list1[len(list1)-1] + list_sum(list1[0:len(list1)-1])
  

list_sum([1,2,3,4,5])