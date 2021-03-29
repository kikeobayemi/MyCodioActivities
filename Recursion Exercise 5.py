def get_max(list1):
  """Return the largest number in a list"""
  if len(list1) == 1:
    return list1[0]
  else:
     return max(list1[0], get_max(list1[1:]))
    
get_max([1,2,3,4,5])