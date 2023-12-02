file = open("data/day1.txt").read()
lines = [x for x in file.split('\n')]

# Part 1
sum = 0
for line in lines:
  nums = [i for i in line if i.isdigit()]
  sum += int(nums[0] + nums[-1])

print("Part 1: "+ str(sum))

# Part 2
ans = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in lines:
  dig = []
  for i, char in enumerate(line):
    if(char.isdigit()):
      dig.append(char)
    for j, val in enumerate(numbers):
      if(line[i:].startswith(val)):
        dig.append(str(j+1))
  ans += int(dig[0]+dig[-1])

print("Part 2: "+ str(ans))