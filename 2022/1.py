file = open('input.txt')
elf = [0]
tmp = 0

for line in file.readlines():
    if line == "\n":
        elf.append(0)
        tmp += 1
    else:
        elf[tmp] += int(line)

elf.sort(reverse=True) 
print(max(elf))
print(sum(elf[:3]))
file.close()