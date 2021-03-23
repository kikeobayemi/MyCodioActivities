#Create a nested loop that produces the output below.
#....1
#...2
#..3
#.4
#5
x=4
while x >0 and x <5:
  for row in range(1,6):
    for column in range(1):
      print("." * x + str(row))
      x-=1