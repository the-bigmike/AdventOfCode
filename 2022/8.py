data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

matrix = []
for line in lines:
  matrix.append(line)

directions = [(-1,0),(1,0),(0,1),(0,-1)]
rows = len(matrix)
columns = len(matrix[0])
count = 0

for row in range(rows):
  for column in range(columns):
    vis = False
    for (dr, dc) in directions:
      rr = row
      cc = column
      ok = True
      while True:
        rr += dr
        cc += dc
        if not (0<=rr<rows and 0<=cc<columns):
          break
        if matrix[rr][cc] >= matrix[row][column]:
          ok = False
      if ok:
        vis = True
    if vis:
      count += 1
print('p1:',count)

topScore = 0
for row in range(rows):
  for column in range(columns):
    score = 1
    for (dr, dc) in directions:
      distance = 1
      rr = row + dr
      cc = column + dc
      while True:
        if not (0<=rr<rows and 0<=cc<columns):
          distance -= 1
          break
        if matrix[rr][cc] >= matrix[row][column]:
          break
        distance += 1
        rr += dr
        cc += dc
      score *= distance
    topScore = max(topScore, score)

print('p2:',topScore)