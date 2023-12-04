import re

file = open("data/day4.txt")
data = file.read()
lines = [x for x in data.split('\n')]

sum1 = 0
cards = [1 for i in lines]
for i, line in enumerate(lines):
  score = 0
  info = re.split(":\s|\s\|\s", line)
  winningNumbers = re.findall("\d+", info[1])
  values = re.findall("\d+", info[2])
  for number in winningNumbers:
    if(values.__contains__(number)):
      score += 1
  if(score > 0):
    sum1 += pow(2, score-1)
    j = 0
    while j < score:
      j += 1
      cards[j+i] += cards[i]

print(f'Part 1: {sum1}')
print(f'Part 2: {sum(cards)}')

file.close()