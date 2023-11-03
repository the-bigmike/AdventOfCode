file = open('input.txt')
score = 0

for line in file.readlines():
  hand = line.split(' ')
  match hand[0]:
    case 'A':
      match hand[1].rstrip('\n'):
        case 'Y':
          score += 1
          score += 3
        case 'Z':
          score += 2
          score += 6
        case 'X':
          score += 3
    case 'B':
      match hand[1].rstrip('\n'):
        case 'X':
          score += 1
        case 'Y':
          score += 2
          score += 3
        case 'Z':
          score += 3
          score += 6
    case 'C':
      match hand[1].rstrip('\n'):
        case 'Z':
          score += 1
          score += 6
        case 'X':
          score += 2
        case 'Y':
          score += 3
          score += 3

print(score)
file.close()