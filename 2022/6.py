data = open('input.txt').read()

def repeat(data, length):
    index = 0
    while len(set(data[index:index+length])) != length:
        index += 1
    print("Task result: " + str(index+length))

repeat(data, 4)
repeat(data, 14)