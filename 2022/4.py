file = open('input.txt')
delimiters = ['-',',']

def contain():
  count = 0

  for line in file.readlines():
    info = line.replace('-',' ').replace(',',' ').split()
    if int(info[0]) <= int(info[2]) and int(info[1]) >= int(info[3]):
      count += 1
    elif int(info[0]) >= int(info[2]) and int(info[1]) <= int(info[3]):
      count += 1

  file.seek(0)
  return count

def overlap():
  count = 0

  for line in file.readlines():
    info = line.replace('-',' ').replace(',',' ').split()
    if int(info[1]) >= int(info[2]) and int(info[0]) <= int(info[3]):
      count += 1

  file.seek(0)
  return count

print('Contain:', contain())
print('Overlap:', overlap())
file.close()