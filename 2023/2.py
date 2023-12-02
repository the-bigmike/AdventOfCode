import re

file = open("data/day2.txt")
data = file.read()
lines = [x for x in data.split('\n')]

sum1 = 0
sum2 = 0
for line in lines:
  good = True
  red, blue, green = [],[],[]
  info = re.split(":|;", line)
  game = re.search("\d+", info[0]).group()
  for i in info[1::]:
    if(i.__contains__("red")):
      red.append(int(re.search("(\d+)\sred", i).group(1)))
      if(int(re.search("(\d+)\sred", i).group(1)) > 12):
        good = False
    if(i.__contains__("blue")):
      blue.append(int(re.search("(\d+)\sblue", i).group(1)))
      if(int(re.search("(\d+)\sblue", i).group(1)) > 14):
        good = False
    if(i.__contains__("green")):
      green.append(int(re.search("(\d+)\sgreen", i).group(1)))
      if(int(re.search("(\d+)\sgreen", i).group(1)) > 13):
        good = False
  if(good):
    sum1 += int(game)
  power = max(red) * max(blue) * max(green)
  sum2 += power

print("Part 1: "+ str(sum1))
print("Part 2: "+ str(sum2))
file.close()