data = open('input.txt').readlines()
count = 0
print(data)

for i in range(len(data)):
  for j in range(len(data[i])):
    if data[i][j] == '\n':
      break
    if i == 0 or i == len(data[i])-1 or j == 0 or j == len(data)-1:
      count += 1
    else:
      print(data[i][j])
print(count)