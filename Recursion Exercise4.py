def reverse_string(my_string):
  """Reverses a string"""
  if len(my_string) == 1:
    return my_string
  else:
    return my_string[len(my_string)-1] +  reverse_string(my_string[0:len(my_string)-1])
  
reverse_string("cat")