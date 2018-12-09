import numpy as np

print ("This is the assignment for December 3rd")

file = open("3.txt", "r")
sheet = np.zeros((1000,1000))

for line in file:
    parts = line.split(' ')
    pos = parts[2][:-1].split(',')
    size = parts[3][:-1].split('x')
    sheet[int(pos[0]):(int(pos[0])+int(size[0])),int(pos[1]):(int(pos[1])+int(size[1]))] += 1

total = (sheet > 1).sum()
#107633

print ("The answer for part a:")
print (total)

file = open("3.txt", "r")

for line in file:
    parts = line.split(' ')
    pos = parts[2][:-1].split(',')
    size = parts[3][:-1].split('x')
    if (sheet[int(pos[0]):(int(pos[0])+int(size[0])),int(pos[1]):(int(pos[1])+int(size[1]))] != 1).sum() == 0:
        print ("The answer for part b:")
        print (parts[0])
        break



