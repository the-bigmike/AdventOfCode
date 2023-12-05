import re

file = open("data/day5.txt")
data = file.read()
lines = re.split("\n\n", data)
print(lines)

seeds, seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHum, humToLoc = [], [], [], [],[] ,[], [],[]
for i, line in enumerate(lines):
  if(line.startswith("seeds:")):
    seeds = line.split(" ")
    seeds.pop(0)
    print(seeds)
  elif(line.startswith("seed-to-soil map:")):
    seedToSoil = re.split("\n|\s", line)
    seedToSoil.pop(0)
    seedToSoil.pop(0)
    print(seedToSoil)
  elif(line.startswith("soil-to-fertilizer map:")):
    soilToFert = re.split("\n|\s", line)
    soilToFert.pop(0)
    soilToFert.pop(0)
    print(soilToFert)
  elif(line.startswith("fertilizer-to-water map:")):
    fertToWater = re.split("\n|\s", line)
    fertToWater.pop(0)
    fertToWater.pop(0)
    print(fertToWater)
  elif(line.startswith("water-to-light map:")):
    waterToLight = re.split("\n|\s", line)
    waterToLight.pop(0)
    waterToLight.pop(0)
    print(waterToLight)
  elif(line.startswith("light-to-temperature map:")):
    lightToTemp = re.split("\n|\s", line)
    lightToTemp.pop(0)
    lightToTemp.pop(0)
    print(lightToTemp)
  elif(line.startswith("temperature-to-humidity map:")):
    tempToHum = re.split("\n|\s", line)
    tempToHum.pop(0)
    tempToHum.pop(0)
    print(tempToHum)
  elif(line.startswith("humidity-to-location map:")):
    humToLoc = re.split("\n|\s", line)
    humToLoc.pop(0)
    humToLoc.pop(0)
    print(humToLoc)


file.close()