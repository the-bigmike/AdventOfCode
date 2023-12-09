file = open("data/day9.txt")
input = file.read().split("\n")

lines = []
for line in input:
  tmp = list(map(int, line.split()))
  lines.append(tmp)

def nextNumber(line):
  current = line
  lineDiff = [line]
  while any(current):
    next = diffList(current)
    lineDiff.append(next)
    current = next
  lineDiff[-1].append(0)
  for i in range(len(lineDiff)-1):
    lineDiff[-i-2].append(lineDiff[-i-2][-1]+lineDiff[-i-1][-1])
    lineDiff[-i-2].insert(0, lineDiff[-i-2][0]-lineDiff[-i-1][0])
  return lineDiff[0][-1], lineDiff[0][0]

def diffList(list):
  diffs = []
  for i in range(len(list) - 1):
    diffs.append(list[i+1] - list[i])
  return diffs

count1 = 0
count2 = 0
for line in lines:
  tmp = nextNumber(line)
  count1 += tmp[0]
  count2 += tmp[1]

print(f'Part 1: {count1}')
print(f'Part 2: {count2}')
file.close()