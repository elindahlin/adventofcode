print("This is the assignment for December 2nd")

file = open("2.txt", "r")

total2 = 0
total3 = 0

for line in file:
    checked = set()
    counted2 = 0
    counted3 = 0
    for char in line:
        if char not in checked:
            count = line.count(char)
            checked.add(char)
            if count == 2 and counted2 == 0:
                total2 += 1
                counted2 = 1
            elif count == 3 and counted3 == 0:
                total3 += 1
                counted3 = 1

print ("Result part a:")
print (total2*total3)

file = open("2.txt", "r")
lines = file.readlines()
length = len(lines)

print ("Result part b:")
for i in range(length-1):
    thisChars = list(lines[i])
    for j in range(i+1,length):
        otherChars = list(lines[j])
        new_list = [ord(a) - ord(b) for a, b in zip(thisChars, otherChars)]
        diff = 0
        for num in new_list:
            if num != 0:
                diff += 1
        if diff == 1:
            print (thisChars)
            print (otherChars)
            print (lines[i])
            break
    else:
        continue
    break
    
