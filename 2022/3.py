file = open('input.txt')
values = ["a",'b',"c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def common():
  count = 0
  for line in file.readlines():
    length = line.rstrip().__len__()
    tmp1 = line[0:int(length/2)]
    tmp2 = line[int(length/2): length]

    found = False
    for i in tmp1:
      for j in tmp2:
        if(i == j):
          found = True
          common = i
          break
      if found:
        count += values.index(common)+1
        break
  file.seek(0)
  return count

def groups():
  count = 0
  lines = file.readlines()
  for i, line in enumerate(lines):
    if i % 3 == 0:
      found = False
      line1 = lines[i].rstrip()
      line2 = lines[i+1].rstrip()
      line3 = lines[i+2].rstrip()
      for x in line1:
        for y in line2:
          if x == y and not found:
            for z in line3:
              if x == z and not found:
                found = True
                common = x
      count += values.index(common)+1
      
  file.seek(0)
  return count

print(common())
print(groups())
file.close()