from copy import deepcopy

data = open('input.txt').read()
lines = [x for x in data.split('\n')]
start = []
commands = []

for line in lines:
  if line == '':
    break
  size = (len(line)+1)//4
  while len(start) < size:
    start.append([])
  for i in range(size):
    container = line[1+4*i]
    if container != ' ' and 'A'<=container<='Z':
      start[i].append(container)

found = False
s1 = deepcopy(start)
s2 = deepcopy(start)
print(s2)
for cmd in lines:
  if cmd == '':
    found = True
    continue
  if not found:
    continue
  command = cmd.split()
  qty = int(command[1])
  from_ = int(command[3])-1
  to_ = int(command[5])-1
  for i in range(qty):
    print(qty, from_, to_)
    s1[to_].insert(0,s1[from_].pop(0))
    s2[to_].insert(i, s2[from_].pop(0))
    print(s2)

print(''.join([s[0] for s in s1]))
print(''.join([s[0] for s in s2]))
