file = open("data/day6.txt")
data = file.read()
lines = [x for x in data.split('\n')]

times = lines[0].split()
dist = lines[1].split()

p2_time, p2_dist = '', ''
num_ways = 1
for i in range(1, len(times)):
    # Part 1 calculation
    count = 0
    tmp_time = 0
    while tmp_time < int(times[i]):
        if(tmp_time * ((int(times[i])) - tmp_time) > int(dist[i])):
            count += 1
        tmp_time += 1
    num_ways *= count

    # Part 2 calculation
    p2_time = p2_time + times[i]
    p2_dist = p2_dist + dist[i]

tmp_time = 0
count = 0
while tmp_time < int(p2_time):
    if(tmp_time * ((int(p2_time)) - tmp_time) > int(p2_dist)):
        count += 1
    tmp_time += 1

print(f'Part 1 = {num_ways}')
print(f'Part 2 = {count}')
file.close()